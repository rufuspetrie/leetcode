# Initial thoughts
    # Few possibilities for greedy algorithm
        # station with most gas
        # station with adjacent having lowest cost[i+1]
        # station with max(gas - cost[i+1])
# Better approach
    # Each of these guesses may fail, so need to test all indexes
    # Notice that this problem boils down to keeping a positive prefix sum
        # for the entire array
    # Note that if a certain start point fails at a particular index, all
        # start points in that interval will also fail
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