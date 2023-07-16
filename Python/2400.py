# How many different ways can you pick the number of steps to the target
    # half the number of remaining steps?
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        steps = abs(endPos - startPos)
        rem = k - steps
        if rem < 0 or rem % 2 != 0: return 0
        return comb(k, steps+rem//2) % MOD