# Initial thoughts
    # Can use something like a sorted list but two heaps is better
# Algorithm
    # Have the higher half of the numbers in a min heap
    # Have the lower half of the numbers in a max heap
    # If the sizes ever differ by more than one, move numbers around
class MedianFinder:

    def __init__(self):
        self.h_heap = []
        self.l_heap = []

    def addNum(self, num: int) -> None:
        if not self.h_heap:
            heappush(self.h_heap, num)
        elif num < self.h_heap[0]:
            heappush(self.l_heap, -num)
        else:
            heappush(self.h_heap, num)
        
        if len(self.l_heap) < len(self.h_heap) - 1:
            heappush(self.l_heap, -heappop(self.h_heap))
        if len(self.h_heap) < len(self.l_heap) - 1:
            heappush(self.h_heap, -heappop(self.l_heap))

    def findMedian(self) -> float:
        if len(self.h_heap) == len(self.l_heap):
            return 0.5 * (self.h_heap[0] - self.l_heap[0])
        else:
            if len(self.h_heap) > len(self.l_heap): return self.h_heap[0]
            else: return -self.l_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()