# Initial thoughts
    # Seems like you can do minimum spanning tree, but painful
    # Dijkstra is probably easier
# Modified Dijkstra
    # Because we only need most expensive node, can return final time
        # instead of keeping track of all node minimum times
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, c in times:
            graph[s].append((c, d))
        
        time = 0
        visited = set()
        heap = [(0, k)]
        while heap:
            cost, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            time = cost

            for cx, nx in graph[node]:
                if nx not in visited:
                    heappush(heap, (cost + cx, nx))

        if len(visited) < n: return -1
        return time