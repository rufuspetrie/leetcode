class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n < 3: return 1
        a = 1
        b = 1
        for i in range(n-2):
            b, a = b+a, b
        return b