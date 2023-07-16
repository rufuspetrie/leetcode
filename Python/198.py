# Base case - one house - robber robs the only house
# Inductive step: robbing marginal house means that robber can't rob adjacent house
    # Therefore, r(i) = max(r(i-1), p(i) + r(i-2))
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        loots = nums[:2]
        for i in range(2, len(nums)):
            loots.append(max(nums[i] + max(loots[:i-1]), loots[i-1]))
        return max(loots[-1], loots[-2])

# Note: 
# Originally had loots.append(max(nums[i] + loots[i-2], loots[i-1]))
# This gave 3 for [2,1,1,2] when the answer is obviously 4
# Because we are only restricted to not robbing houses adjacent to the marginal one,
# we can take loot from ANY of the previous maxes, not just odd/even patterns