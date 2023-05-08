# Thoughts
    # Similar to subarray meeting condition hard problem
    # Keep track of last non-zero value
    # Calculate number of zero arrays terminating at each index
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        last_nonzero = -1
        total = 0
        for i, n in enumerate(nums):
            if n != 0: last_nonzero = i
            total += i - last_nonzero

        return total