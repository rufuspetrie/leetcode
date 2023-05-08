# Algorithm:
    # (n & 1) extracts value from lowest bit
    # (n >> 1) shifts bits over one, thus removing the lowest bit
    # repeat process recursively until the number equals zero
class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            total += (n & 1)
            n >>= 1
        return total