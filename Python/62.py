# Notes
    # Can just do a combinatorial solution
    # Should probably check back and see if other solutions are interesting
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1)
    
"""
The proper (read: slow) DP solution is basically simplified edit distance
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        for i in range(m): dp[i][0] = 1
        for i in range(n): dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
"""