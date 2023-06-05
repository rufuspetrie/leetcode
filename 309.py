# Initial thoughts
    # Seems similar to house robber problem - cooldown like adjacent house rule
    # Need 2D DP - one dimension equals buy days, one equals sell days?
    # Useful to draw decision tree - choices are always buy/sell or cooldown
        # because you can only own one stock at a time
    # Caching solution - increment i by 1 if buy, 2 if sell,
        # keep a boolean denoting buy/sell
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        DP = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in DP:
                return DP[(i, buying)]
            
            # At each state, recursively determine the maximum profit
                # from either waiting or buying/selling
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                DP[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                DP[(i, buying)] = max(sell, cooldown)
            
            return DP[(i,buying)]

        return dfs(0, 1)