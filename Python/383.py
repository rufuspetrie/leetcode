class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in range(len(magazine)):
            if magazine[i] in d.keys(): d[magazine[i]] += 1
            else: d[magazine[i]] = 1
        for i in range(len(ransomNote)):
            if ransomNote[i] in d.keys() and d[ransomNote[i]] > 0:
                d[ransomNote[i]] -= 1
            else:
                return False

        return True