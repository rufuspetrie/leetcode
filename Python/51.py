# Algorithm
    # Keep track of the current queen columns by using array
        # (it's a given that they'll be in different rows)
    # Also need to keep track of diagonals that queens attack
        # For increasing diagonals, r+c remains the same
        # For decreasing diagonals, r-c remains the same
    # At each step, if the number of queens placed equals n, return the board
    # Otherwise, find viable positions from column/diagonal information and place queens
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

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
        return solutions