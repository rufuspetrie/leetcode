# Initial thoughts
    # Code binary search in such a way that it returns index of first occurence
    # Find first occurence, then perform binary search on resulting subarray
class Solution:
    def binarysearch(self, nums, target):
        l = 0
        r = len(nums) - 1
        mid = 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = self.binarysearch(nums, target)
        if low == -1: return [-1, -1]
        high = low

        while low > 0 and nums[low-1] == nums[low]: low -= 1
        while high < len(nums) - 1 and nums[high+1] == nums[high]: high += 1

        return [low, high]