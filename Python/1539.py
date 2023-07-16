class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        arr = set(arr)
        s = [i for i in range(1, arr[-1]) if i not in arr]

        if k <= len(s):
            return s[k-1]
        if not s:
            return arr[-1] + k
        else:
            return arr[-1] + k - len(s)