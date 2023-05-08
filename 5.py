# Initial thoughts
    # Need to iterate through and check for palindromes centered at each index
    # While elements are equal, expand a pointer left and right from the element
    # Because palindromes can have a middle element, need to do two passes and check
        # for palindromes of each style (e.g. xSx, xSSx)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        idx = 0
        len_x = 0

        # Middle element
        for i in range(n):
            lp, rp = i, i
            while lp >= 0 and rp < n and s[lp] == s[rp]:
                if rp - lp + 1 > len_x: 
                    len_x = rp - lp + 1
                    idx = lp
                lp -= 1
                rp += 1

        # No middle element
        for i in range(n):
            lp, rp = i, i + 1
            while lp >= 0 and rp < n and s[lp] == s[rp]:
                if rp - lp + 1 > len_x:
                    len_x = rp - lp + 1
                    idx = lp
                lp -= 1
                rp += 1

        return s[idx:idx+len_x]