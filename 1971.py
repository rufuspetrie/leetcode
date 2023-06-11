class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, v in edges:
            graph[i].append(v)
            graph[v].append(i)

        visited = set()
        def dfs(start):
            if start == destination:
                return True
            if start not in visited:
                visited.add(start)
                for i in graph[start]:
                    if dfs(i):
                        return True
            return False

        return dfs(source)