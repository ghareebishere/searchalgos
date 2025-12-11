# utils/generator.py
import random
from typing import List

def generate_random_list(size: int, min_val: int = 0, max_val: int = 100, sorted: bool = False) -> List[int]:
    """
    Generate a random list of integers.
    Args:
        size (int): The number of elements in the list.
        min_val (int, optional): The minimum value for random integers. Defaults to 0.
        max_val (int, optional): The maximum value for random integers. Defaults to 100.
        sorted (bool, optional): Whether to return a sorted list. Defaults to False.
    Returns:
        List[int]: A list of random integers.
    """
    """"""
    if sorted:
        data = [random.randint(min_val, max_val) for _ in range(size)]
        data.sort()
    else:
        data = [random.randint(min_val, max_val) for _ in range(size)]

    return data