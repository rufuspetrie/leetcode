# Initial thoughts
    # Any positive prefix adds to sum, so just accumulate sum while positive
    # Compare max at each step
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for i in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += i
            max_sum = max(current_sum, max_sum)

        return max_sum