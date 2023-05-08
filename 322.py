# Initial thoughts
    # Make dynamic problem going until value
    # Fill in dynamic program by dividing value by coin amounts
    # Update DP by allowing combination values
# Problem
    # No need to fill in all multiples of coin values for DP, only base cases
    # From there, iteratively fill in by subtracting coin values and checking whether
        # they're in the dynamic program
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        if amount == 0: return 0
        dp = [0 for i in range(amount+1)]
        for i in range(len(dp)):
            if i in coins: 
                dp[i] = 1
            else:
                for c in coins:
                    if i - c > 0 and dp[i - c]:
                        if not dp[i]:
                            dp[i] = 1 + dp[i - c]
                        else:
                            dp[i] = min(dp[i], 1 + dp[i - c])
        
        if not dp[-1]: return -1
        return dp[-1]