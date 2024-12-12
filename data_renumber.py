import sys

def renumber_edges(edge_list):
    # Extract all unique nodes from the edge list
    nodes = set()
    for edge in edge_list:
        nodes.update(edge)

    # Create a mapping of old node values to new progressive numbers
    node_mapping = {node: i + 1 for i, node in enumerate(sorted(nodes))}

    # Renumber the edges according to the mapping
    renumbered_edges = [
        (node_mapping[edge[0]], node_mapping[edge[1]]) for edge in edge_list
    ]

    return renumbered_edges


def read_edges_from_file(input_file):
    edges = []
    with open(input_file, "r") as file:
        for line in file:
            edge = tuple(map(int, line.split()))
            edges.append(edge)
    return edges


def write_edges_to_file(output_file, edge_list):
    with open(output_file, "w") as file:
        for edge in edge_list:
            file.write(f"{edge[0]} {edge[1]}\n")


# Ensure the script is executed with the correct arguments
if len(sys.argv) != 3:
    print("Usage: python data_renumber.py <input_file> <output_file>")
    sys.exit(1)

# Read the input and output file names from sys.argv
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read edges from the input file
edge_list = read_edges_from_file(input_file)

# Renumber the edges
renumbered_edges = renumber_edges(edge_list)

# Write the renumbered edges to the output file
write_edges_to_file(output_file, renumbered_edges)
print(f"Renumbered edges written to {output_file}")
