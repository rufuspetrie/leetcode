import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            if i in d.keys(): d[i] -=1
            else: d[i] = -1
        x = []
        for i in d.items():
            heappush(x, i[::-1])
        out = []
        for i in range(k):
            out.append(heappop(x)[1])
        return out