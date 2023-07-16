# Initial thoughts
    # Everything that's a power of 2 will only have one bit
    # Pattern: 0 1 1 2 1 2 2 3 1 . . .
    # Notice: you repeat a lot of work when doing binary representations because
        # each time you gain a significant bit, you're just adding the old bit
        # representations to the new ones (e.g. 9 = 1001 = 1000 + 0001)
    # Therefore, can use DP
        # Each time you reach a new power of two, need to double lookback
class Solution:
    def countBits(self, n: int) -> List[int]:
        DP = [0 for i in range(n+1)]
        lookback = 1

        for i in range(1, n+1):
            if lookback * 2 == i: lookback = i
            DP[i] = 1 + DP[i - lookback]

        return DP