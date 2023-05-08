class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        if numRows == 1: return out
        for i in range(1, numRows):
            new_row = [1]
            for i in range(len(out[-1]) - 1):
                new_row.append(out[-1][i] + out[-1][i+1])
            new_row.append(1)
            out.append(new_row)

        return out