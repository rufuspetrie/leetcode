class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        re = ""
        px = 0
        while px < len(word1) and px < len(word2):
            re += word1[px]
            re += word2[px]
            px += 1
        if px < len(word1): re += word1[px:]
        if px < len(word2): re += word2[px:]
        return re