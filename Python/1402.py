# Initial thoughts
    # Sort satisfactions
    # It's worth including negative dishes if their value is less than the
        # sum of all the positive dishes
# Correction
    # It's worth including negative dishes while the sum of their values
        # is less than the sum of the positive dishes
# Easier method
    # Iterate backwards from tail of sorted array
    # While sum of numbers is positive, advance pointer
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if not satisfaction: return 0
        satisfaction.sort()

        # Iterate backwards while sum of elements > 0
        cur = 0
        idx = len(satisfaction)
        while idx > 0 and cur >= 0:
            if cur + satisfaction[idx - 1] > 0:
                cur += satisfaction[idx - 1]
                idx -= 1
            else:
                break

        # Perform necessary sum
        total = 0
        x = 1
        for i in satisfaction[idx:]:
            total += x * i
            x += 1

        return total