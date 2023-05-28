# Initial thoughts
    # Iterate through grid and search if not in explored
    # For BFS/DFS, return number of nodes visited
    # Compare with max after each search
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        explored = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols \
            or (r,c) in explored or grid[r][c] == 0:
                return 0
            else:
                explored.add((r,c))
                return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        c_max = 0
        for r in range(rows):
            for c in range(cols):
                c_max = max(c_max, dfs(r,c))

        return c_max