# Initial thoughts
    # can just iterate over rows and binary search each row
# Better algorithm
    # note that starting from the top left, moving in any direction
        # will increase matrix[i][j]
    # however, if you start from the bottom left, moving up will decrease
        # the value and moving right will increase the value
    # therefore, you can just do linear search from the bottom left and
        # it will be faster than iterative binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        i = rows - 1
        j = 0

        while i >= 0 and j < cols:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1

        return False