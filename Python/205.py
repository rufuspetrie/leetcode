# Initial thoughts
    # Create mapping between s and t
    # While creating it, return false if a letter is already mapped
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        d = {}
        for i in range(len(s)):
            if t[i] not in d.keys():
                if s[i] in d.values(): return False
                else: d[t[i]] = s[i]
        tt = "".join([d[i] for i in list(t)])
        print(tt)
        return s == tt