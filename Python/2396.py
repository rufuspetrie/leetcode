# This is always false
    # Consider what it means to have a number in base n-2
    # The 1 bit ranges from 0 to (n-2), and the 1 bit ranges from 0 to (n-2)**2
    # Clearly, every time we use this base, our number will have value 12
    # Therefore, no number fits this criteria
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False