# Initial thoughts
    # Seems like modified Dijkstra/Bellman-Ford
    # Dijkstra TLE'd so trying Bellman-Ford
    # Can implement BF much simpler than other traversal algorithms
        # by using a temporary cost list for each step
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf") for i in range(n)]
        cost[src] = 0

        for i in range(k + 1):
            temp = cost[:]
            for s, d, c in flights:
                if cost[s] == float("inf"):
                    continue
                if cost[s] + c < temp[d]:
                    temp[d] = cost[s] + c
            cost = temp

        if cost[dst] == float("inf"):
            return -1
        return cost[dst]