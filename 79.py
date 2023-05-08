# Backtracking solution
    # Base cases - string == word or out of bounds, invalid character, etc
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(idx, r, c):
            if idx == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or (r,c) in path or board[r][c] != word[idx]):
                return False
            else:
                path.add((r,c))
                res = (dfs(idx + 1, r + 1, c)
                    or dfs(idx + 1, r - 1, c)
                    or dfs(idx + 1, r, c + 1)
                    or dfs(idx + 1, r, c - 1))
                path.remove((r,c))
                return res

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False