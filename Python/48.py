# Initial thoughts
    # Algorithm is to rotate cells in groups of 4
    # Easier to do with r/l pointers and while loops instead of iteratively
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix[0]) - 1

        while l < r:
            for i in range(r - l):
                top = l
                bottom = r
                temp = matrix[top][l+i]

                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = temp
            
            r -= 1
            l += 1

        return 0