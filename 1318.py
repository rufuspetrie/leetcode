# Initial thoughts
    # Note that we use INCLUSIVE-OR for this problem
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while a or b or c:
            if (c & 1):
                res += not (a & 1) and not (b & 1)
            else:
                res += (a & 1) + (b & 1)
                
            a >>= 1
            b >>= 1
            c >>= 1

        return res