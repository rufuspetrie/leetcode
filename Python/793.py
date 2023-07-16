# 0 <= k <= 10**9
# Given a trailing number of zeros k, find the number of factorial functions with this number of zeros
# Note: https://leetcode.com/problems/factorial-trailing-zeroes/description/ might be useful
# Original attempt (TLE'd)
    # Iterate through multiples of 5
    # Add # of 5's in PF of i to total
    # Check whether the total ever equals k
# Binary search:
    # For arbitrary factorials, can check the number of 0's with zeros function
    # Lower bound: 0
    # Upper bound: 10*k because f(n) picks up a factor of 5 (and thus a zero)
        # slightly more often than every 5th factorial
class Solution:

    # Return number of zeros of factorial(n)
    def zeros(self, n: int) -> int:
        total = 0
        base = 5
        while base <= n:
            total += n // base
            base *= 5
        return total

    # Binary search
    def preimageSizeFZF(self, k: int) -> int:
        if k == 0: return 5
        l = 0
        r = k*10
        while l < r:
            mid = (l + r)//2
            if self.zeros(mid) == k:
                return 5
            elif self.zeros(mid) < k:
                l = mid + 1
            elif self.zeros(mid) > k:
                r = mid -1

        return 0