# Initial thoughts
    # Use max heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapify(nums)
        x = nums[0]
        for i in range(k):
            x = -heappop(nums)
        return x