# Initial thoughts
    # Valid trees are connected and have no cycles
    # Can do Union Find and check parent set length
    # Can also do DFS traversal and check for n nodes, n-1 edges
class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graph = {i: [] for i in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in graph[node]:
                dfs(node)

        dfs(graph[edges[0][0]])
        return len(visited) == n and len(edges) == (n - 1)      