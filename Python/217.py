class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                return True
        return False