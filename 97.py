# Initial thoughts
    # Could potentially do two pointer solution, but could take long
    # Notice that this becomes a problem when characters at an index are equal,
        # so you need to backtrack regardless
    # At each index (i,j), we can select s1[i+1] or s2[j+1] to add to the string
    # Therefore, can visualize the DP problem as a decision tree where you
        # shift one of the two pointers based on equality
# Algorithm
    # Use top down 2d-DP where (i,j) represents the index of each respective string
    # If we can match the character at s1[i]/s2[j] to s3[i+j], we can mark that
        # cell true and continue iterating backwards
    # This lets us attempt different series of interleavings for equilvalent
        # characters when traversing the two strings
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        DP = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        DP[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and DP[i + 1][j]:
                    DP[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and DP[i][j + 1]:
                    DP[i][j] = True

        return DP[0][0]