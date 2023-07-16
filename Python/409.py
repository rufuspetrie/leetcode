class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        flag = False
        max_len = 0
        for i in d.keys():
            if d[i] % 2 != 0:
                flag = True
            max_len += (d[i]//2)*2

        return max_len + flag