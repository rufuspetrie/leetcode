class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(len(nums)):
            if target < nums[i]:
                return i
        return len(nums)