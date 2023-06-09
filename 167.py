# Notice: can do this like regular two-sum problem
    # can also do a two pointer method because the array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1

        return [l+1, r+1]