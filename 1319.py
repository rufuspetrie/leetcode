# Initial thoughts
    # Use BFS, subtract length of visited nodes from n
# After first try
    # Need to find the number of connected components
    # There can be multiple, so need to start DFS from every unexplored node
from collections import deque
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        visited = [0] * n
        graph = [set() for _ in range(n)]
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)

        def dfs(self, node):
            if visited[node] == 1:
                return 0
            visited[node] = 1
            for i in graph[node]:
                dfs(self, i)
            return 1

        component_count = 0
        for i in range(n): component_count += dfs(self, i)
        return component_count - 1