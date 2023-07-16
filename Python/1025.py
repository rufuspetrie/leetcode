# Can always make an even number odd by subtracting 1
# Odd numbers always have two odd factors, so can always turn odd numbers even
# If you start with even, can ensure that the number stays even by always
    # subtracting 1 after your partner's turn
# If you start odd, your partner can always force you to even
# Therefore, whoever starts even wins, odd loses
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2 == 0:
            return True
        else:
            return False