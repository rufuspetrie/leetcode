class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        total = 0
        for i in range(len(num)):
            total += num[i]*10**(len(num)-i-1)
        total += k
        total = map(int, [i for i in str(total)])
        return total