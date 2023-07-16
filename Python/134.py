# Initial thoughts
    # Greedy: could start at lowest cost, most gas, greatest difference
# Better approach
    # Each of these guesses may fail, so need to test multiple indexes
    # Notice that this problem boils down to keeping a positive prefix sum
        # for the entire array
    # Note that if a certain start point fails at a particular index, all
        # start points in that interval will also fail (Kadane's algorithm)
    # Clarification: gas[i] = cost to travel to i + 1, not cost to travel to
        # i from i - 1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        tank = 0
        idx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        return idx