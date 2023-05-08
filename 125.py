# Notes
    # A lot of the methods used to clean up strings take forever
    # Therefore, it's a lot faster to use two pointers and skip over
        # junk characters manually
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = s.lower()
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True