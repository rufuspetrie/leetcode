# Algorithm
    # Make graph into an undirected graph but keep a set of the original roads
    # Do dfs (parent, child)
        # If the path is in roads, it doesn't need to be flipped
        # Otherwise, add 1 to the flip count
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        roads = set()
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
            roads.add((i, j))

        self.flip_count = 0

        def dfs(child, parent):
            if (parent, child) in roads: self.flip_count += 1
            for i in graph[child]:
                if i != parent:
                    dfs(i, child)

        dfs(0, -1)
        return self.flip_count