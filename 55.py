# Notes
    # Greedy approach: advance and increment remaining jumps upward when you hit a higher value
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