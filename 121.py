class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_min = prices[0]
        max_p = 0
        for p in prices:
            if p < p_min: p_min = p
            max_p = max(max_p, p - p_min)

        return max_p