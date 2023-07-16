# Algorithm:
    # Creating array of prefixes/suffixes doesn't work so well because there are annoying edge cases
    # It's easier to create an output array and modifier it while traversing nums
    # Note: original intuition correct - just annoying to populate arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0]*n

        prod = 1
        for i in range(n):
            output[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(n - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]

        return output