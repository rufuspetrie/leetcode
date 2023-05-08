# Notes
    # Can just do a combinatorial solution
    # Should probably check back and see if other solutions are interesting
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1)