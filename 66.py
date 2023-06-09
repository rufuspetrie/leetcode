# Initial thoughts
    # may be easier to reverse digits
    # need to condition on whether idx equals length of digits
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        carry = 1
        while carry:
            if idx >= 0:
                if digits[idx] == 9:
                    digits[idx] = 0
                else:
                    digits[idx] += 1
                    carry = 0
            else:
                digits = [1] + digits
                carry = 0
            idx -= 1

        return digits