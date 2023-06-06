# Initial thoughts
    # Set grid[0][0] to 1 after you check it for an obstacle, can reuse as DP
    # Similar to the original paths problem but need to set obstacle cells to 0
        # manually when you iterate and find them
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1: return 0
        else: grid[0][0] = 1

        for i in range(1, rows):
            grid[i][0] = int(grid[i][0] == 0 and grid[i-1][0] == 1)

        for i in range(1, cols):
            grid[0][i] = int(grid[0][i] == 0 and grid[0][i-1] == 1)

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[i][j] == 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                else:
                    grid[i][j] = 0
        
        print(grid)
        return grid[rows - 1][cols - 1]