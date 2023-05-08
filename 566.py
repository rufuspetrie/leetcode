class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])
        if rows*cols != r*c:
            return mat
        
        new_mat = [[0]*c for i in range(r)]
        old_mat = mat[0]
        for i in mat[1:]:
            old_mat += i

        for i in range(len(old_mat)):
            new_mat[i//c][i%c] = old_mat[i]

        return new_mat