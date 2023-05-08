# What screwed everything up with this problem?
    # When you notice floating points coming into a problem, deal with them
        # immediately instead of letting the errors accumulate
    # For instance, you saw floating points coming up when dividing by factorials
    # You should have just used integer division there instead of waiting until
        # the end to use int() - this allowed the error term to start growing
from math import factorial
class Solution:
    def anagrams(self, word):
        
        # Count duplicates
        d = {}
        for i in word:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        d = [d[i] for i in d.keys() if d[i] > 1]
        
        # Return unique permutations
        total = factorial(len(word))
        for i in d: total //= factorial(i)
        return total
        
    def countAnagrams(self, s: str) -> int:
        MOD = (10**9 + 7)
        total = 1
        for i in s.split(): total *= self.anagrams(i)
        return int(total % MOD)