# main.py
from utils.generator import generate_random_list
from src.listBased import binary_search, linear_search
import time

def main():
    print("--- Search Algorithm Project ---")
    
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

if __name__ == "__main__":
    main()