# Initial thoughts
    # Can't use binary because reversed binary doesn't imply reverse decimal
    # Therefore, just solve using modulus/remainders
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