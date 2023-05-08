# Notes
    # Have left pointer and right pointer
    # While sum of subarray is positive, advance right pointer only
    # Once subarray becomes negative, move left pointer to next positive number
    # pointers/while too slow so need to use iterative approach
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