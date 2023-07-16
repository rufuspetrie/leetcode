# Return nearest closest 0
# First attempt:
    # Iterate through entire matrix and perform BFS for each column - TLE'd
# Alternative approach:
    # Instead of starting from 1's and finding 0's, start from 0's and find 1's
        # With this approach, can put all 0 values into queue and run BFS once
        # At each matrix entry, can update it to equal 1 + (value of previous node)
        # This successfully tracks the number of steps from a 0 it takes to reach the node
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        visited = set()
        
        # Add all zero values to queue/visited
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        # Perform BFS on queue
        while queue:
            i, j = queue.popleft()
            for d in directions:
                ix = i + d[0]
                jx = j + d[1]
                if ix >= 0 and ix < rows and jx >= 0 and jx < cols and (ix,jx) not in visited:
                    mat[ix][jx] = mat[i][j] + 1
                    queue.append((ix,jx))
                    visited.add((ix,jx))

        return mat