import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            cur = -heappop(stones)
            heappush(stones, -1*abs(cur + heappop(stones)))
        return -1*heappop(stones)