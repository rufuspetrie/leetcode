# Use BFS, have initial queue as all infected oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        queue = []
        fresh = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0: return 0
        if not queue: return -1

        time = -1
        while queue:
            time += 1
            new_queue = []
            for i, j in queue:
                if i > 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    new_queue.append((i-1, j))
                if i < r - 1 and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    new_queue.append((i+1, j))
                if j > 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    new_queue.append((i, j-1))
                if j < c - 1 and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    new_queue.append((i, j+1))
            queue = new_queue

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1

        return time