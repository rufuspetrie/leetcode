# Algorithm:
#   Keep queue of elements in sliding window
#   At any time, the queue must be in decreasing order (max at x[0])
#   To add new item, pop from end of queue until new element is less than end of queue
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        x = deque([0])
        maxes = []
        
        # Set up initial deque
        for i in range(1, k):
            while x and nums[i] > nums[x[-1]]:
                x.pop()
            x.append(i)
        maxes.append(nums[x[0]])

        # Slide window
        for i in range(k, len(nums)):
            while x and nums[i] > nums[x[-1]]:
                x.pop()
            # Check whether x[0] still in window
            if x and x[0] <= i-k:
                x.popleft()
            x.append(i)
            maxes.append(nums[x[0]])

        return maxes