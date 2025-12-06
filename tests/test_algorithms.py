# tests/test_algorithms.py
import unittest
from src.listBased import linear_search, binary_search, jump_search
from src.graphBased import bfs, dfs

class TestListSearches(unittest.TestCase):
    
    def setUp(self):
        # We use a fixed sorted list for consistent testing
        self.sorted_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.unsorted_data = [50, 10, 40, 20, 30]

    def test_linear_search(self):
        self.assertEqual(linear_search(self.unsorted_data, 40), 2)
        self.assertEqual(linear_search(self.unsorted_data, 999), -1)

    def test_binary_search(self):
        # Binary search MUST utilize sorted data
        self.assertEqual(binary_search(self.sorted_data, 30), 2)
        self.assertEqual(binary_search(self.sorted_data, 10), 0)
        self.assertEqual(binary_search(self.sorted_data, 100), 9)
        self.assertEqual(binary_search(self.sorted_data, 999), -1)

    def test_jump_search(self):
        self.assertEqual(jump_search(self.sorted_data, 70), 6)
        self.assertEqual(jump_search(self.sorted_data, 999), -1)

class TestGraphSearches(unittest.TestCase):
    
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [], 'E': [], 'F': []
        }

    def test_bfs(self):
        self.assertTrue(bfs(self.graph, 'A', 'E'))
        self.assertFalse(bfs(self.graph, 'A', 'Z'))

    def test_dfs(self):
        self.assertTrue(dfs(self.graph, 'A', 'F'))
        self.assertFalse(dfs(self.graph, 'A', 'Z'))

if __name__ == '__main__':
    unittest.main()