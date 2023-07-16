# Notes
    # Might be better to just use a set so you can skip filtering the negatives
import heapq
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 1
        nums = list(set(nums))
        heapify(nums)
        while nums and nums[0] < 1:
            heappop(nums)
        cur_max = 0
        while nums and nums[0] == cur_max + 1:
            cur_max = heappop(nums)

        return cur_max + 1