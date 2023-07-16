# Initial thoughts
    # Can reuse longest palindromic subarray code here
    # Can stop tracking subarray length and add to pal_count each time
        # the while loop stays valid
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        idx = 0
        pal_count = 0

        # Middle element in palindrome
        for i in range(n):
            lp, rp = i, i
            while lp >=0 and rp < n and s[lp] == s[rp]:
                pal_count += 1
                lp -= 1
                rp += 1
        
        # No middle element
        for i in range(n):
            lp, rp = i, i + 1
            while lp >=0 and rp <n and s[lp] == s[rp]:
                pal_count += 1
                lp -= 1
                rp += 1

        return pal_count