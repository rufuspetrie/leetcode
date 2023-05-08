import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(i) for i in nums]
        heapify(nums)
        x = nums[0]
        for i in range(k):
            x = -heappop(nums)
        return str(x)