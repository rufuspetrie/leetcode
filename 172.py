# Observations:
    # all values of the factorial function greater than f(1) are even
    # the is a 0 every time there is both a 2 and 5 in the PF of f(n)
    # there are always strictly more 2's than 5's in the PF of f(n)
    # therefore, f(n) gains a 0 for every 5, two for 25's, three for 125's etc
    # Thus, the problem becomes counting the number of 125's in the PF of f(n)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        total = 0
        base = 5
        while base <= n:
            total += n // base
            base *= 5

        return total