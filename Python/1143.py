# Initial thoughts
    # Inclusion/exclusion scheme doesn't work because the strings both
        # have 2^l1/2^l2 configurations
    # Therefore, think of the DP as 2 dimensions with each index interpreted
        # as the LCS from a particular index onward
    # If characters at the given index (i,j) match, then the LCS equals
        # 1 + LCS(i+1, j+1)
    # If characters at the given index (i,j) do not match, then the LCS
        # equals max(LCS(i+1,j), LCS(i,j+1)), the left and downward entries
# Notice that this is basically the same as the edit distance except we
# populate the array from the end of the substrings
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        DP = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    DP[i][j] = 1 + DP[i+1][j+1]
                else:
                    DP[i][j] = max(DP[i+1][j], DP[i][j+1])

        return DP[0][0]