# algorithms/list_search.py
import math
from typing import List, Optional

def linear_search(arr: List[int], target: int) -> int:
    """
    Iterates through the list one by one.
    Returns index if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    """
    Requires a SORTED list. Divide and conquer approach.
    Returns index if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def jump_search(arr: List[int], target: int) -> int:
    """
    Requires a SORTED list. Jumps ahead by fixed steps, then does linear search.
    Optimal step size is sqrt(n).
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Finding the block where element is present (if it is present)
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
            
    # Linear search for target in block beginning with prev
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
            
    if arr[prev] == target:
        return prev
        
    return -1