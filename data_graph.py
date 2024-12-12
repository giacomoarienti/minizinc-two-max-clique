import sys
import openpyxl


def edge_list_to_adjacency_matrix(edge_list_file, output_xlsx_file):
    # Read the edge list from the file
    with open(edge_list_file, "r") as file:
        edges = [line.strip().split() for line in file.readlines()]

    # Extract unique nodes from the edge list
    nodes = set()
    for edge in edges:
        nodes.update(edge)

    # Sort the nodes to ensure consistency in the adjacency matrix
    nodes = sorted(nodes)

    # Create a dictionary to map node labels to matrix indices
    node_index = {node: idx for idx, node in enumerate(nodes)}

    # Initialize an empty adjacency matrix with 0s
    n = len(nodes)
    adjacency_matrix = [[0] * n for _ in range(n)]

    # Fill the adjacency matrix based on the edges
    for edge in edges:
        node1, node2 = edge
        index1 = node_index[node1]
        index2 = node_index[node2]
        adjacency_matrix[index1][index2] = 1
        adjacency_matrix[index2][index1] = 1  # Assuming undirected graph

    # Create an Excel workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Adjacency Matrix"

    # Write the header with node labels
    ws.append([""] + nodes)

    # Write the adjacency matrix with node labels
    for i, row in enumerate(adjacency_matrix):
        ws.append([nodes[i]] + row)

    # Save the workbook to the specified file
    wb.save(output_xlsx_file)


# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python data_graph.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

edge_list_to_adjacency_matrix(input_file, output_file)
