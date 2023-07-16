# Initial thoughts
    # Note subarray - must be contiguous elements
    # Seems simliar to maximum sum subarray
        # Fails - can't discard negative cumulative products e.g. [-2,3,-4]
    # Brute force: find product of every possible subarray
        # Working bottom up - repeats a lot of work when increasing subarray sizes
# Pattern
    # Solving this problem efficiently requires working with patterns of negatives
    # With all positives, can just take largest subarray, need to be careful with negatives
    # To avoid negative issues, keep track of both max/min subarray
        # In case of negative marginal values, min times the negative can be greater
        # than the current maximum
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        res = nums[0]

        for n in nums:
            temp = n * cur_max
            cur_max = max(n, n * cur_min, n * cur_max)
            cur_min = min(n, n * cur_min, temp)
            res = max(res, cur_max)

        return res