# Initial thoughts
    # regular coin change: minimum coins required to make x
    # brute force: decision tree, count # of leaves equal to x
        # for each branch, only choose coins >= current to avoid duplicates
# DP setup
    # for the DP, need (a, i) a denotes the sum you're trying to reach
        # and i denotes the index of the coin you use
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)