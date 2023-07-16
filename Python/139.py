# Initial thoughts
    # Need to scan word instead of constructing list of possible words because
        # words can be used repeatedly like example 2
    # Can make decision tree where branches are words from dictionary
        # if word is a string prefix, advance pointer past the word
        # if substring not in dictionary, mark index as false in DP
            # and revert the pointer
# Algorithm
    # Work backwards from the end of the word, with DP[len] = 1
    # Iterate backwards and see if a word in the dictionary is in str[i:]
        # If it's less than the substring length, check str + dp[i+l]
        # to see if the rest of the substring is matched
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        DP = [0 for i in range(n+1)]
        DP[-1] = 1

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    DP[i] = DP[i + len(word)]
                if DP[i]:
                    break

        return DP[0]