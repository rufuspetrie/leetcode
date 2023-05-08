# Algorithm
    # Initialize reversed number to 0
    # For each of the 32 bits:
        # Left shift the reversed number 1
        # Add the lowest bit of n to n_rev
        # Right shift 
    # Note: left shift before the changes to avoid another shift after the final operation
class Solution:
    def reverseBits(self, n: int) -> int:
        n_rev = 0
        for i in range(32):
            n_rev <<= 1
            n_rev ^= (n & 1)
            n >>= 1

        return n_rev