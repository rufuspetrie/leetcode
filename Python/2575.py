class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        d_array = []
        n_array = []
        # for i in range(len(word)):
            
        for i in range(len(word)):
            if int(word[:i+1]) % m == 0:
                d_array.append(1)
            else:
                d_array.append(0)
        return d_array