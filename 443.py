# Note that for a solution we need to modify the input array in-place

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 1
        i = 0
        j = 0

        while i < len(chars):

            k = 1
            while i < len(chars) - 1 and chars[i] == chars[i+1]:
                i += 1
                k += 1

            chars[j] = chars[i]
            j += 1

            if k > 1:
                for l in str(k):
                    chars[j] = l
                    j += 1

            i += 1
        
        return j