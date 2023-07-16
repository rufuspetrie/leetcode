# Algorithm:
    # Need variables to keep track of board (row, column, square)
    # Box id: use (row//3*3 + col//3) ==> this maps from 0-8 for the squares
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        # Constraint variables
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]
        
        # Add initial board configuration to sets
        for r in range(n):
            for c in range(n):
                if board[r][c] != ".": 
                    rows[r].add(int(board[r][c]))
                    cols[c].add(int(board[r][c]))
                    boxes[r//3*3 + c//3].add(int(board[r][c]))

        def place_number(r, c):
            
            # Is the board solved already?
            nonlocal done
            if r == 9:
                done = True
                return

            # Next location to place numbers
            next_r = r + (c + 1) // 9
            next_c = (c + 1) % 9

            # If (r,c) is filled, proceed to next cell
            if board[r][c] != ".":
                place_number(next_r, next_c)
            else:
                for i in range(1, 10):
                    if i not in rows[r] and i not in cols[c] and i not in boxes[r//3*3 + c//3]:
                        
                        rows[r].add(i)
                        cols[c].add(i)
                        boxes[r//3*3 + c//3].add(i)
                        board[r][c] = str(i)
                        place_number(next_r, next_c)

                        if not done:
                            rows[r].remove(i)
                            cols[c].remove(i)
                            boxes[r//3*3 + c//3].remove(i)
                            board[r][c] = "."

        done = False
        place_number(0, 0)