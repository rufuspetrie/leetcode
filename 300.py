# Initial thoughts
    # Note: subsequence ==> elements may not be contiguous
    # Brute force: generate every subsequence and check if increasing
        # Repeats work because have to scan each element of each new sequence
        # Not really amenable to caching because the DP requires 2^n entries
    # Generating all subsequences yields a decision tree like other DP problems
# Algorithm
    # Top down DP with 1d array (values initialized to 1)
    # Iterate backwards through array
        # At each index, check all later DP values
        # If they're larger, compare 1 + DP[L] to DP[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = [1 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    DP[i] = max(DP[i], 1 + DP[j])
        return max(DP)