# Initial thoughts
    # Note: subsequences ==> don't have to be contiguous
    # Seems like 2d-DP, let (i,j) equal the characters at index i/j
        # Iterate through strings and match characters
        # When a match fails, move the s pointer but don't move t because it's required
    # Notice that you need to find all ways of matching and not just one match,
        # so need to take sums of (i+1,j+1) and (i+1,j)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        DP = {}
        for i in range(len(s) + 1):
            DP[(i, len(t))] = 1
        for j in range(len(t)):
            DP[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    DP[(i,j)] = DP[(i + 1, j + 1)] + DP[(i + 1, j)]
                else:
                    DP[(i,j)] = DP[(i+1, j)]

        return DP[(0,0)]