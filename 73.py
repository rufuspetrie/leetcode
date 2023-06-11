# Initial thoughts
    # Scan row/col for zero and set first entry to zero if you find one
    # When flipping zeros, iterate from 1 onward
    # Notice that if mat[0][0] is 0, then every cell will be flipped,
        # so need special case to determine if first row is all 0s
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        zero = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        zero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if zero:
            for c in range(cols):
                matrix[0][c] = 0