# Initial thoughts
    # solution has to be some type of bit shenanigans
    # in particular, likely need to process sum bits (XOR) and carries (AND) separately
    # Note: it's convenient to do XOR's and AND's at the same time and then
        # shift the AND's left once so they carry properly
    # Algorithm: compute bits and carries
        # recursively add the bits to carries until the carries equal 0
        # note: this is a bit of a headache in python because of no static types
class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(a, b):
            if not a or not b:
                return a or b
            return add((a & b) << 1, a ^ b)

        if a * b < 0:
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:
                return 0
            if add(~a, 1) < b:
                return add(~add(add(~a, 1), add(~b, 1)), 1)
        
        return add(a, b)