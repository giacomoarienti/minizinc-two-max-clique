# Max Clique Problem - MiniZinc Model

This project contains a MiniZinc model designed to solve the **Max Clique Problem** with a specific variation: 

**"Can you find two disjoint cliques such that the overall number of selected clique nodes is maximized?"**

The project is structured as follows:

## Project Structure

```
|── data
│   ├── 50_edges.mzn      # MiniZinc model data for 50 edges
│   ├── 50_edges.txt      # Example input file for the model
│   └── 5_nodes.dzn       # Data in MiniZinc format for 5 nodes
├── data_convert.py       # Python script to convert edge list to MiniZinc input format
└── max_clique.mzn        # Basic MiniZinc model for solving the Max Clique Problem
```

### Files Overview

1. **`data/`**:
   - This folder contains example datasets to feed into the MiniZinc model.
   - **`50_edges.mzn`**: Example MiniZinc file containing data for a graph with 50 edges.
   - **`50_edges.txt`**: Text file containing an edge list where each line represents an edge in the form "start_node end_node".
   - **`5_nodes.dzn`**: MiniZinc data file for a graph with 5 nodes.

2. **`data_convert.py`**:
   - This Python script converts a text file containing edge lists into a MiniZinc input file (`.mzn` format).
   - The script expects input data in the form:
     ```
     1 2
     1 3
     2 4
     ```
     Where each line represents an edge from a starting node to an ending node.
   - To use the script, run:
     ```
     python3 data_convert.py input.txt output.mzn
     ```

3. **`max_clique.mzn`**:
   - The basic MiniZinc model for solving the Max Clique Problem.
   - You can run the model using:
     ```
     minizinc max_clique.mzn input.mzn
     ```
   - The model finds the largest clique in the given graph.

4. **Variation Work-in-Progress**:
   - The variation on the Max Clique Problem that focuses on finding two disjoint cliques with the overall maximum number of nodes is still under development.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository_url>
   ```

2. Convert the input data using the Python script:
   ```
   python3 data_convert.py data/50_edges.txt output.mzn
   ```

3. Run the basic Max Clique model:
   ```
   minizinc max_clique.mzn output.mzn
   ```

4. The variation model is under development and will be available soon.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.