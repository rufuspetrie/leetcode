# Initial thoughts
    # Can extract smallest bit with &1
    # Can rightshift to delete former smallest big
    # Can |(b<<31) to insert the smallest bit at the beginning of the number
    # Note: for python reasons, easier to just treat number as decimal instead of binary
class Solution:
    def reverse(self, x: int) -> int:
        int_min = -1 * 2**31
        int_max = 2**31 - 1

        res = 0
        while x:
            bit = int(math.fmod(x, 10))
            x = int(x / 10)
            if res > int_max // 10 or (res == int_max // 10 and bit > int_max % 10):
                return 0
            if res < int_min // 10 or (res == int_min // 10 and bit < int_min % 10):
                return 0
            res = (res * 10) + bit

        return res