# Note
    # My old code restarted the string 1 after the first instance when it found a duplicate
    # This is better because instead of restarting, it just moves the left pointer past
        # the first occurence of the duplicate
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)

        l = 0
        r = 0
        x = set(s[0])
        max_len = 0

        while r < len(s) - 1:
            r += 1
            while s[r] in x:
                x.remove(s[l])
                l += 1
            x.add(s[r])
            max_len = max(max_len, len(x))

        return max_len