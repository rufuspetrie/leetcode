# Initial thoughts
    # After making graph with l1 distances, it's just minimum spanning
    # Expectedly, TLE's just using input list - must use graph
# Improvements
    # Instead of using has with heaps for each point,
        # just make hash with graph[point] = [dist, point]
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        res = 0
        visited = set()
        heap = [[0, 0]]

        while len(visited) < n:
            cost, idx = heappop(heap)
            if idx in visited:
                continue
            res += cost
            visited.add(idx)
            for ncost, nidx in graph[idx]:
                if nidx not in visited:
                    heappush(heap, [ncost, nidx])
        
        return res