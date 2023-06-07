# Initial thoughts
    # Seems like unique paths but use min instead of sum
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        DP = [[0] * cols for i in range(rows)]
        DP[0][0] = grid[0][0]

        for i in range(1, rows):
            DP[i][0] = DP[i-1][0] + grid[i][0]

        for j in range(1, cols):
            DP[0][j] = DP[0][j-1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]

        return DP[rows - 1][cols - 1]