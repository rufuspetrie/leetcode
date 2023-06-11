class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, v in edges:
            graph[i].append(v)
            graph[v].append(i)

        n = len(graph.keys())
        for i in graph.keys():
            if len(graph[i]) == n - 1:
                return i

        return 0