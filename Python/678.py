# Initial thoughts
    # Keep track of the number of each type of parenthesis (o = 1, c = -1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        o = 0
        c = 0
        for char in s:
            o += 1 if char == "(" else -1
            c += 1 if char != ")" else -1
            if c < 0: break
            o = max(o, 0)

        return o == 0