class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n == 1: return 1
        vals = set()
        print(ceil(sqrt(9)))
        for i in range(1, ceil(sqrt(n) + 1)):
            if n % i == 0:
                vals.add(i)
                vals.add(n//i)

        vals = sorted(vals)
        if k <= len(vals): return vals[k - 1]
        else: return -1