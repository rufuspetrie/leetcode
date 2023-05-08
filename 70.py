# Notes 
#   at each step, you have two possible ways of reaching that step
#       namely, you can either onestep from the previous or twostep from 2 before
#   therefore, the solution closely resembles the fibonacci sequence
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 2
        for i in range(n-2):
            b, a = a+b, b
        return b