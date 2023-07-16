# Initial thoughts
    # Probably 2d-DP of some kind
    # Without ./* it's regular string matching
    # . can match with anything, * can match while element is the same
    # note that ./* can match empty strings as well as characters
    # Need DP for this problem because you can match * to multiple characters,
        # which spawns a decision tree for repeated matchings
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        DP = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        DP[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) -1, -1, -1):
                match = (i < len(s)) and (s[i] == p[j] or p[j] == ".")
                if (j + 1) < len(p) and p[j + 1] == "*":
                    DP[i][j] = DP[i][j + 2]
                    if match:
                        DP[i][j] = DP[i + 1][j] or DP[i][j]
                elif match:
                    DP[i][j] = DP[i + 1][j + 1]

        return DP[0][0]