class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        k = -2
        for i in range(len(piles)//3):
            total += piles[k]
            k-=2
        return total