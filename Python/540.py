# To the left of the single element, first elements are even indexed, second odd
# To the right of the single element, first elements are odd indexed, second even
# Therefore, do binary search on even indexed numbers and check if the next number is equal
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums)
        val = 0
        
        while l <= r:
            # m = midpoint, rx = highest even indexed number
            m = (l+r)//2
            rx = m * 2
            if rx + 1 >= len(nums) or nums[rx] != nums[rx+1]:
                r = m - 1
                val = nums[rx]
            else:
                l = m + 1
        
        return val