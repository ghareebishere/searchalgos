# utils/generator.py
import random
from typing import List

def generate_random_list(size: int, min_val: int = 0, max_val: int = 100) -> List[int]:
    """Generates a list of random integers."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_sorted_list(size: int, min_val: int = 0, max_val: int = 100) -> List[int]:
    """Generates a sorted list of random integers (Required for Binary Search)."""
    data = generate_random_list(size, min_val, max_val)
    data.sort()
    return data