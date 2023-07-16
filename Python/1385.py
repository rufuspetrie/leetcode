class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        total = len(arr1)
        arr2 = sorted(arr2)
        for i in arr1:
            if abs(i-arr2[0]) <= d or abs(i-arr2[-1]) <= d:
                total -= 1
        
        return total