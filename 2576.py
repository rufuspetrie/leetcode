class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:     
        
        nums = sorted(nums)
        total = 0
        lp = 0
        rp = len(nums)//2
        print(nums)
        
        while rp < len(nums):
            if 2*nums[lp] <= nums[rp]:
                lp += 1
                rp += 1
                total += 2
            else:
                rp += 1
        
        return total