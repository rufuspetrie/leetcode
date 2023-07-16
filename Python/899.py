# Algorithm
    # k = 1 - can rotate array
    # k > 1 - can sort array
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(list(s)))
        
        min_s = s
        for i in range(len(s)):
            s = s[1:] + s[0]
            min_s = min(s, min_s)
        
        return min_s