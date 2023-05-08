class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high < low:
            return 0
        
        # Cases: odd/odd, odd/even, even/odd, even/even

        if low%2 == 0 and high%2 == 0:
            return((high-low)//2)
        
        return((high-low)//2 + 1)