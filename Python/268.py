# Initial thoughts
    # Can probably use XOR b/c if you flip the bits once for each val in nums
        # and once for each val in range(n+1), the missing number will be the remainder
    # Need to start at 0
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0
        for i in range(len(nums)+1): val ^= i
        for i in nums: val ^= i
        return val