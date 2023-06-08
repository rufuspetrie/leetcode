class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        base = [[1], [1, 1]]
        if rowIndex <= 1: return base[rowIndex]
        for i in range(1, rowIndex):
            res = [1]
            for j in range(len(base[-1]) - 1):
                res.append(base[-1][j] + base[-1][j + 1])
            res.append(1)
            base.append(res)

        return base[-1]