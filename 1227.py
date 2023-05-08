# N passengers board an airplane with n seats
# Probability that nth person gets his own seat?
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n < 2: return 1
        else: return 0.5