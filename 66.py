# Initial thoughts
    # may be easier to reverse digits
    # need to condition on whether idx equals length of digits
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = 0
        carry = 1
        digits = digits[::-1]

        while carry:
            if idx < len(digits):
                if digits[idx] == 9:
                    digits[idx] = 0
                else:
                    digits[idx] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            idx += 1

        return digits[::-1]