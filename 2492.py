# First thoughts
    # Do BFS and keep track of minimum edge
from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for (i, j, k) in roads:
            graph[i][j] = k
            graph[j][i] = k
        min_edge = float("inf")
        visited = set([1])
        queue = deque([1])

        while queue:
            cur = queue.popleft()
            for node, length in graph[cur].items():
                if node not in visited: 
                    queue.append(node)
                    visited.add(node)
                min_edge = min(min_edge, length)

        return min_edge