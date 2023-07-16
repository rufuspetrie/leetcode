# Dynamic programming solution
# Memoization matrix: dp[i][j] represents the steps required to change the substring
#   str1[i:] to str[j:]
#   We start by initializing this matrix to [[0,1,2,3], [1,0,0,0], [2,0,0,0], ...]
#   because we can trivially find the steps required to change each substring size
#   to an empty string.
#   From there, we can fill in each cell by comparing the strings at the index
#   and seeing whether the character is equal.
#   If equal, no change is required, so dp[i][j] = dp[i-1][j-1]
#   (steps required to make strings equal without the latest character)
#   If unequal, find the minimum steps required to make equal by performing a
#   deletion, insertion, or replacement
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # Set up memoization matrix
        x = len(word1)
        y = len(word2)
        dp = [[0]*(y+1) for i in range(x+1)]

        # Base case - steps required to make string empty
        for i in range(1, x+1):
            dp[i][0] = i
        for i in range(1, y+1):
            dp[0][i] = i

        # Fill in rest of matrix based on character parity
        for i in range(1, x+1):
            for j in range(1, y+1):

                # Equal characters
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # Unequal characters
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        print(dp)
        return dp[x][y]