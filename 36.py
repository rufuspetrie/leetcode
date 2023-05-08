# Note
    # For checking the squares, need nice way to map coordinates to corresponding squares
    # The function idx = r//3*3 + c//3 gives such an index
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check whether squares are fine
        squares = {}
        for r in range(9):
            for c in range(9):
                idx = r//3*3 + c//3
                if idx not in squares.keys():
                    squares[idx] = [board[r][c]]
                else:
                    if board[r][c] != "." and board[r][c] in squares[idx]:
                        return False
                    squares[idx] += [board[r][c]]

        # Check whether rows are fine
        for r in range(9):
            x = set()
            for c in range(9):
                if board[r][c] != "." and board[r][c] in x:
                    return False
                else:
                    x.add(board[r][c])

        # Check whether columns are fine
        for c in range(9):
            x = set()
            for r in range(9):
                if board[r][c] != "." and board[r][c] in x:
                    return False
                else:
                    x.add(board[r][c])

        return True