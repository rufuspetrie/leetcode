# Note
    # Iterative solution failed even though it should be faster in theory
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]