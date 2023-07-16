# Initial thoughts
    # If even power, return x^(n/2) * x^(n/2)
    # If odd power, return x * x^(n-1)
# Problem
    # Returning x * x^(n-1) causes TLE, need more efficient method
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = pow(x*x, n//2)
            return x * res if n % 2 else res

        res = pow(x, abs(n))
        return res if n > 0 else 1 / res