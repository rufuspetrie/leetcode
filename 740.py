# This is similar to the house robber problem
# In this problem, taking a number causes all adjacent numbers to be deleted
# However, iterating through the array like the robber problem will not work
# Unlike before, adjacent values can be equal, so you need to consider more simultaneously
# Therefore, a better approach is to make an array of value counts and iterate over that array instead
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        value_counts = [0]*(max(nums)+1)
        for i in nums:
            value_counts[i] += 1
        print(value_counts)
        
        profits = value_counts[:2]
        for i in range(2, len(value_counts)):
            profits.append(max(profits[i-1], i*value_counts[i] + max(profits[:i-1])))

        return profits[-1]