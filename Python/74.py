# Note: you can just view the matrix as a m*n long array
    # (much simpler than doing binary search on rows then column)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        r = len(matrix)
        c = len(matrix[0])
        
        l = 0
        r = r*c-1
        while l <= r:
            m = (l + r)//2
            m_val = matrix[m//c][m%c]
            if m_val == target:
                return True
            elif m_val < target:
                l = m + 1
            else:
                r = m - 1

        return False