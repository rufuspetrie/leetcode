# Initial thoughts
    # Can just iterate through matrix and count all negatives
    # Alternately, can use binary search to find first negative entry 
        # for each row/column
    # Alternately, can linearly search for first negative in each row
        # and return number of remaining entries
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for row in grid:
            l = 0
            r = cols - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] < 0:
                    r = m - 1
                else:
                    l = m + 1
            res += (cols - l)
        
        return res