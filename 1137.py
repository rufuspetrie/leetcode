class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n < 3: return 1
        a = 0
        b = 1
        c = 1
        for i in range(n-2):
            c, b, a = c+b+a, c, b
        return c