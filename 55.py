# Initial thoughts
    # Keep track of jumps remaining and current index
    # Advance pointer through array and update jump count if greater than current value
    # If pointer advances past len(array) - 1, return true
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        idx = 0
        while jumps > 0 and idx < len(nums) - 1:
            idx += 1
            jumps -= 1
            if nums[idx] > jumps:
                jumps = nums[idx]
        return idx == (len(nums) - 1)