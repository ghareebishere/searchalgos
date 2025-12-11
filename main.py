# main.py
from utils.generator import generate_random_list
from src.listBased import binary_search, linear_search
from src.graphBased import bfs, dfs

import time

def main():
    print("--- Search Algorithms ---")
    
    # 1. Generate Data
    dataset_size = 100000
    print(f"Generating sorted dataset of {dataset_size} items...")
    data = generate_random_list(dataset_size, 0, 200000, sorted=True)
    target = data[-1] # Pick the last element to force worst-case for Linear Search
    
    print(f"Targeting value: {target}")
    print("-" * 30)

    # 2. Run Linear Search
    start_time = time.perf_counter()
    idx_lin = linear_search(data, target)
    end_time = time.perf_counter()
    print(f"Linear Search: Found at index {idx_lin} in {end_time - start_time:.6f} seconds")

    # 3. Run Binary Search
    start_time = time.perf_counter()
    idx_bin = binary_search(data, target)
    end_time = time.perf_counter()
    print(f"Binary Search: Found at index {idx_bin} in {end_time - start_time:.6f} seconds")



    print("--- Graph Search Algorithms ---")
    
    # 1. Define Hardcoded Data
    print("Loading  graph data...")
    
    # A graph with multiple paths, dead ends, and cycles
    # Nodes are integers 0-15
    graph_data = {
        0: [1, 5, 2],
        1: [3, 4],
        2: [5, 6],
        3: [7, 8],
        4: [8, 9],
        5: [10, 11],
        6: [11, 2],      # Cycle back to 2
        7: [12],
        8: [12, 13],
        9: [13],
        10: [14],
        11: [14, 5],     # Cycle back to 5
        12: [15],
        13: [15],
        14: [15],
        15: []           # Target
    }
    
    start_node = 0
    target_node = 15
    
    print(f"Graph loaded with {len(graph_data)} nodes.")
    print(f"Targeting node: {target_node} starting from {start_node}")
    print("-" * 30)

    # 2. Run Breadth-First Search (BFS)
    start_time = time.perf_counter()
    found_bfs = bfs(graph_data, start_node, target_node)
    end_time = time.perf_counter()
    
    status_bfs = "Found" if found_bfs else "Not Found"
    print(f"BFS: {status_bfs} target in {end_time - start_time:.6f} seconds")

    # 3. Run Depth-First Search (DFS)
    start_time = time.perf_counter()
    found_dfs = dfs(graph_data, start_node, target_node)
    end_time = time.perf_counter()
    
    status_dfs = "Found" if found_dfs else "Not Found"
    print(f"DFS: {status_dfs} target in {end_time - start_time:.6f} seconds")



if __name__ == "__main__":
    main()