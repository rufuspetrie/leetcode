# Initial thoughts
    # Idea: instead of figuring out all regions, figure out regions
        # that can't be surrounded
    # start from O's on the border and do DFS on them to find cells
        # that can't be surrounded, and flip them to T's
    # Flip all remaining O's to X's, then change T's to O's
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[1,0], [-1,0], [0,-1], [0,1]]
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return
            board[r][c] = "T"
            for i, j in dirs:
                dfs(r + i, c + j)

        # Flip O's connected to the border
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r == 0 or r == rows - 1 \
                or c == 0 or c == cols - 1):
                    dfs(r,c)

        # Flip remaining O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Unflip T's to O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"