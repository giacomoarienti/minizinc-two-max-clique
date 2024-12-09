/*
   Source from: https://ieeexplore.ieee.org/document/9259673 
   Use Gecode or Gurobi as solver 
*/
include "globals.mzn";

/* Variables */
int: num_nodes;
array[1..num_nodes, 1..num_nodes] of int: g; /* adjacency matrix, g[i, j] = 1 means an edge between nodes i and j */
var set of 1..num_nodes: s; /* solution nodes */
array[1..num_nodes] of var bool: c; /* binary decision variables, c[i] = 1 means node i is in the clique */
var int: size; /* clique size */

/* constraints */
constraint size = sum(c);
/* no two non-adjacent nodes can both be in the clique */
constraint forall(i, j in 1..num_nodes where i != j) (
    0 == g[i, j] -> (c[i] + c[j] <= 1)
);
/* each node is connected to at least one clique member */
constraint link_set_to_booleans(s, c);
/* each node must be adjacent to at least one node in the clique */
constraint forall(j in 1..num_nodes) (
    sum(i in 1..num_nodes) ((1 - g[i, j]) * c[i]) >= 1
);
/* each node must have at least one neighbor in the clique */
constraint forall(i in 1..num_nodes) (
    sum(j in 1..num_nodes) (c[j] * (1 - g[i, j])) > 0
);

/* Objective function */
solve :: int_search(g, input_order, indomain_random, complete)
    maximize size; /* maximize the clique size */

output [
    "Size: ", show(size), "\n",
    "Nodes: ", show([i | i in s]), "\n",
];

