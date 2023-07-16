class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x in points: heappush(heap, ((x[0]**2+x[1]**2)**0.5, x))
        res = []
        for i in range(k): res.append(heappop(heap)[1])
        return res