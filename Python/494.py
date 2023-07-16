# Initial thoughts
    # Seems like backtracking type problem, just find all possible +/- combinations
        # and cache the results
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        DP = {}

        def dfs(idx, sum):
            if idx == len(nums):
                return 1 if sum == target else 0
            if (idx, sum) in DP:
                return DP[(idx, sum)]
            DP[(idx, sum)] = dfs(idx + 1, sum - nums[idx]) \
            + dfs(idx + 1, sum + nums[idx])
            return DP[(idx, sum)]

        return dfs(0, 0)