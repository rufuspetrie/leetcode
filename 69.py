# Notes
    # Try dividing the number by progressively larger numbers
        # until the quotient is less than the divisor
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        flag = True
        i = 1
        while flag:
            flag = False
            if x/(i+1) >= (i+1):
                i += 1
                flag = True
        return i