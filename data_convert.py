import numpy as np
import sys

def convert_to_adjacency_matrix(input_file, output_file):
    # Read the edges from the input file
    edges = []
    with open(input_file, "r") as f:
        for line in f:
            node1, node2 = map(int, line.strip().split(" "))
            edges.append((node1, node2))

    # Find the total number of nodes by getting the maximum node number
    nodes = set()
    for node1, node2 in edges:
        nodes.add(node1)
        nodes.add(node2)

    num_nodes = len(nodes)
    node_list = sorted(nodes)  # Sort to make the node list consistent
    node_index = {node: i for i, node in enumerate(node_list)}

    # Create an empty adjacency matrix
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    # Fill the adjacency matrix based on the edges
    for node1, node2 in edges:
        i = node_index[node1]
        j = node_index[node2]
        adj_matrix[i, j] = 1
        adj_matrix[j, i] = 1  # Since it's an undirected graph

    # Write the adjacency matrix to the output file
    with open(output_file, "w") as f:
        f.write(f"num_nodes = {num_nodes};\n\n")
        f.write("g = array2d(1..num_nodes, 1..num_nodes, [\n")
        for row in adj_matrix:
            f.write("    " + ", ".join(map(str, row)) + ",\n")
        f.write("]);\n")

if len(sys.argv) != 3:
    print("Usage: python data_convert.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

convert_to_adjacency_matrix(input_file, output_file)
