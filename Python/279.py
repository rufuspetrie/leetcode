# Initial thoughts
    # This is basically coin change but the coins are squares
class Solution:
    def numSquares(self, n: int) -> int:
        DP = [0 for i in range(n+1)]
        squares = set()
        x = 1
        while x**2 <= n:
            squares.add(x**2)
            x += 1

        for i in range(1, len(DP)):
            if i in squares:
                DP[i] = 1
                continue
            for s in squares:
                if i - s > 0 and DP[i - s]:
                    if DP[i]:
                        DP[i] = min(DP[i], 1 + DP[i - s])
                    else:
                        DP[i] = 1 + DP[i - s]

        return DP[-1]