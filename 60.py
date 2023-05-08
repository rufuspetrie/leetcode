# Algorithm
    # Determine the "permuation coordinate" of k
    # While k > 0, continually take k//(n-1)!, k//(n-2)!,... etc. to find branch of permutation algorithm
from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        coord = []
        x = n - 1
        k = k - 1
        while k > 0:
            coord.append(k//factorial(x))
            k = k % factorial(x)
            x -= 1

        pre = [str(i) for i in range(1, (n+1))]
        post = []
        for i in coord:
            post += pre.pop(i)
        post += pre
        return "".join(post)