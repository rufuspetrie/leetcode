# Initial thoughts
    # Probably want to use DFS/BFS
    # Iterate through grid
    # If cell is land and unexplored, add 1 to island count
    # Use BFS to mark all cells in the island as visited
# Notes
    # Using directions list and iterating over is easier than manually branching
    # Doing (r) in range(rows) is easier than checking r > 0, r < rows
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    rn, cn = r + dr, c + dc
                    if (rn) in range(rows) and (cn) in range(cols) \
                    and grid[rn][cn] == "1" and (rn,cn) not in visited:
                        queue.append((rn,cn))
                        visited.add((rn,cn))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands