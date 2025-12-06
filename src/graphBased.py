# algorithms/graph_search.py
from typing import List, Dict, Any

# Graph represented as Adjacency List: { 'A': ['B', 'C'], 'B': ['D'], ... }

def bfs(graph: Dict[Any, List[Any]], start_node: Any, target_node: Any) -> bool:
    """Breadth-First Search. Returns True if target is found."""
    visited = []
    queue = [start_node]
    
    while queue:
        node = queue.pop(0) # Pop from front
        if node == target_node:
            return True
        
        if node not in visited:
            visited.append(node)
            # Add neighbors to queue
            if node in graph:
                queue.extend(graph[node])
    return False

def dfs(graph: Dict[Any, List[Any]], start_node: Any, target_node: Any, visited=None) -> bool:
    """Depth-First Search (Recursive). Returns True if target is found."""
    if visited is None:
        visited = set()
        
    if start_node == target_node:
        return True
        
    visited.add(start_node)
    
    if start_node in graph:
        for neighbor in graph[start_node]:
            if neighbor not in visited:
                if dfs(graph, neighbor, target_node, visited):
                    return True
    return False