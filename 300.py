# Initial thoughts
    # Note: subsequence ==> elements may not be contiguous
    # Brute force: generate every subsequence and check if increasing
        # Repeats work because have to scan each element of each new sequence
        # Not really amenable to caching because the DP requires 2^n entries
    # Generating all subsequences yields a decision tree like other DP problems
# Binary search algorithm
    # Start populating a DP with elements of the array
    # If the next element is greater than the final one, insert it
    # If it's less, find the index where it would be in sorted order
        # and replace the element there (this is what bisect_left does)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        DP = []
        for i in nums:
            if not DP or DP[-1] < i:
                DP.append(i)
            else:
                idx = bisect_left(DP, i)
                DP[idx] = i
        
        return len(DP)

"""        
Standard DP algorithm
    Top down DP with 1d array (values initialized to 1)
    Iterate backwards through array
        At each index, check all later DP values
        If they're larger, compare 1 + DP[L] to DP[i]

DP = [1 for i in range(len(nums))]
for i in range(len(nums) - 1, -1, -1):
    for j in range(i + 1, len(nums)):
        if nums[j] > nums[i]:
            DP[i] = max(DP[i], 1 + DP[j])
return max(DP)
"""