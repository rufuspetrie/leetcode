# Algorithm
    # nXORn = 0 for all n
    # XOR is associative, so the bits of all numbers appearing twice will
        # not change the final answer when XORing the entire array
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = nums[0]
        for i in range(1, len(nums)):
            total ^= nums[i]
        return total