class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        k = 0
        while k + len(needle) <= len(haystack):
            if needle == haystack[k:k+len(needle)]: return k
            k += 1
        return -1