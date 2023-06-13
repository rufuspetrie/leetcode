# Initial thoughts
    # Need to find minimum time, so BFS/Dijkstra might work
    # Maybe interpret time as the cost of a node and use Dijkstra?
        # Instead of adding together node costs, just make it the max
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        heap = [[grid[0][0], 0, 0]]

        while heap:
            t, r, c = heappop(heap)
            if r == rows - 1 and c == cols - 1:
                return t
            
            for i, j in dirs:
                x = r + i
                y = c + j
                if x in range(rows) and y in range(cols) and (x,y) not in visited:
                    visited.add((x,y))
                    heappush(heap, [max(t, grid[x][y]), x, y])