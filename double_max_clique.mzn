/*
   Source from: https://ieeexplore.ieee.org/document/9259673 
   Use Gecode or Gurobi as solver 
*/
include "globals.mzn";

/* Variables */
int: num_nodes;
array[1..num_nodes, 1..num_nodes] of int: g; /* adjacency matrix, g[i, j] = 1 means an edge between nodes i and j */

/* Variables for first clique */
var set of 1..num_nodes: s1; /* solution nodes for the first clique */
array[1..num_nodes] of var bool: c1; /* binary decision variables for the first clique */
var int: size1; /* size of the first clique */

/* Variables for second clique */
var set of 1..num_nodes: s2; /* solution nodes for the second clique */
array[1..num_nodes] of var bool: c2; /* binary decision variables for the second clique */
var int: size2; /* size of the second clique */

/* Ensure that nodes in c1 and c2 are disjoint */
constraint forall(i in 1..num_nodes) (
    c1[i] + c2[i] <= 1
);

/* Constraints for the first clique */
constraint size1 = sum(i in 1..num_nodes)(c1[i]);
constraint forall(i, j in 1..num_nodes where i != j) (
    0 == g[i, j] -> (c1[i] + c1[j] <= 1)
);
constraint link_set_to_booleans(s1, c1);

/* Constraints for the second clique */
constraint size2 = sum(i in 1..num_nodes)(c2[i]);
constraint forall(i, j in 1..num_nodes where i != j) (
    0 == g[i, j] -> (c2[i] + c2[j] <= 1)
);
constraint link_set_to_booleans(s2, c2);

/* Objective function: maximize the total size of both cliques */
solve maximize size1 + size2;

/* Output */
output [
    "Size1: ", show(size1), "\n",
    "Nodes in Clique 1: ", show([i | i in s1]), "\n",
    "Size2: ", show(size2), "\n",
    "Nodes in Clique 2: ", show([i | i in s2]), "\n"
];
