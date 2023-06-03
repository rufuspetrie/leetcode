# Initial thoughts
    # Seems like you can do minimum spanning tree, but painful
    # Dijkstra is probably easier
# Dijkstra in plain english
    # Start with beginning node in a heap
    # While the heap still has stuff in it:
        # pop the top of the heap
        # if any neighbors aren't in the cost or the current cost is lower than the old,
            # add them to the heap and update their cost
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, c in times:
            graph[s].append((c, d))
        
        heap = []
        for i in graph[k]:
            heappush(heap, i)

        min_cost = {k: 0}
        while heap:
            cost, node = heappop(heap)
            if node not in min_cost:
                min_cost[node] = cost
            else:
                min_cost[node] = min(min_cost[node], cost)
            for c, d in graph[node]:
                if d not in min_cost:
                    heappush(heap, (c + cost, d))

        if len(min_cost.keys()) < n:
            return -1
        max_cost = 0
        for i in min_cost.keys():
            max_cost = max(max_cost, min_cost[i])
        return max_cost