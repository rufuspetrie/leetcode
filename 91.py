# Initial thoughts
    # Need to use ord() helper functions and stuff probably
    # Issue in the problem lies in where to split the encoded string
        # Can always pick one character substrings if not 0
        # Two character substrings can only map to a letter if <= 26
    # For DP, think of how we can express this using recursion/optimal substructure
        # How does the number of encodings change when we add one number to the end of the string?
        # = numways(i-1) + 1 + numways(i-2) (if new character can encode with the last)
    # Problem: many 0's can make string undecodable, so need way to deal with them
# Algorithm
    # Think of iterating through the string and using an inclusion/exclusion tree
        # like you would for bracktracking
    # The leftmost subtree would be taking characters 1 at a time, and right branches take 2
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        
        # How many ways can you decode the substring starting at index i?
        def dfs(i):
            # Already in DP
            if i in dp.keys(): return dp[i]
            # Does string start with 0?
            if s[i] == "0": return 0

            # Taking character at i as a single digit
            result = dfs(i+1)

            # Can we make i and i+1 into a single digit?
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                result += dfs(i+2)

            dp[i] = result
            return result

        return dfs(0)