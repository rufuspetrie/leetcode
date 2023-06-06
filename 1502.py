# Initial thoughts
    # Sorting solution is easy
    # To sweat it, can rselect x_1/x_2 to find diff and check set inclusion
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 1: return True
        arr.sort()
        d1 = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] != arr[i] + d1:
                return False
        return True