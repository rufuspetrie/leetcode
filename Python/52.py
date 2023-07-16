# Notes
    # Same as previous problem, just return the length of the output instead
class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for i in range(n)]
        solutions = []
        columns = set()
        pos_diag = set()
        neg_diag = set()

        def place_queen(r = 0):
            if r == n:
                solutions.append(["".join(row) for row in board])
            else:
                for c in range(n):
                    # Check whether moves are valid
                    if c in columns or (r+c) in pos_diag or (r-c) in neg_diag:
                        continue
                    else:
                        # Update constraints and place queen
                        columns.add(c)
                        pos_diag.add(r+c)
                        neg_diag.add(r-c)
                        board[r][c] = "Q"
                        place_queen(r+1)
                        
                        # Remove constraints after recursion finishes
                        columns.remove(c)
                        pos_diag.remove(r+c)
                        neg_diag.remove(r-c)
                        board[r][c] = "."

        place_queen()
        return len(solutions)