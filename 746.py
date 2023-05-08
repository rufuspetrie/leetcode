# Initial thoughts
    # Can start at step 0 or 1, so initialize min_cost to [0, 0]
    # From there, the min_cost of each step is the minimum cost of reaching one step
        # before and onestepping and the cost of reaching two steps before and twostepping
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0, 0]
        for i in range(2, len(cost)+1):
            min_cost.append(min(cost[i-1]+min_cost[i-1], cost[i-2]+min_cost[i-2]))
        return min_cost[-1]