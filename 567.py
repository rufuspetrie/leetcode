# What's going on here?
    # Create counter for the first string
    # Iterate through the second string
        # Any time the index gets longer than the length of s1,
            # add the letter now out of range back in to the counter
        # If the counter reaches 0f for all values at any time, return true
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        d = {}
        for i in s1:
            if i not in d.keys(): d[i] = 1
            else: d[i] += 1

        for i in range(len(s2)):
            if s2[i] in d.keys():
                d[s2[i]] -= 1
            if i >= len(s1) and s2[i-len(s1)] in d.keys():
                d[s2[i-len(s1)]] += 1
            if all(d[i] == 0 for i in d.keys()):
                return True

        return False