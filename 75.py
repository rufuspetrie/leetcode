class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0, 0, 0]
        for i in nums:
            if i == 0: counts[0] += 1
            if i == 1: counts[1] += 1
            if i == 2: counts[2] += 1

        
        for i in range(counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[0] + counts[1]):
            nums[i] = 1
        for i in range(counts[0] + counts[1], counts[0] + counts[1] + counts[2]):
            nums[i] = 2