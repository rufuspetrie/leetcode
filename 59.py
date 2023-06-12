# Initial thoughts
    # Similar to original spiral matrix but fill in instead of scanning
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]

        top = 0
        left = 0
        right = n
        bottom = n
        base = 1
        res = [[0] * n for i in range(n)]

        while top < bottom or left < right:
            for i in range(left, right):
                res[top][i] = base
                base += 1
            top += 1

            for i in range(top, bottom):
                res[i][right - 1] = base
                base += 1
            right -= 1

            for i in range(right - 1, left - 1, -1):
                res[bottom - 1][i] = base
                base += 1
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res[i][left] = base
                base += 1
            left += 1

        return res