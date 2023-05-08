"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# Steps:
    # Check if the grid values are equal
    # If so, return node with grid values marked as true
    # If unequal, split grid into four subgrids and repeat procedure

class Solution:
    
    # Call recursive function to split up the grid
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.r_construct(grid, 0, 0, len(grid))

    # Function to check whether elements of current grid are all equal
    def eq(self, grid, x, y, s):
        v = grid[x][y]
        for i in range(x, x+s):
            for j in range(y, y+s):
                if grid[i][j] != v:
                    return False
        return True

    # Construct grid or recursively construct based on eq return
    def r_construct(self, grid, x, y, s):
        
        # All nodes equal - return grid marked as leaf node
        if self.eq(grid, x, y, s):
            return Node(grid[x][y], True)

        # Unequal nodes - split into four subgrids and repeat procedure
        s = s//2
        root = Node(0, False)

        # Nested lists ==> top left unshifted, bottom right x/y shifted
        root.topLeft = self.r_construct(grid, x, y, s)
        root.topRight = self.r_construct(grid, x, y + s, s)
        root.bottomLeft = self.r_construct(grid, x + s, y, s)
        root.bottomRight = self.r_construct(grid, x + s, y + s, s)
        return root