class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            mid = len(nums) // 2
            l = nums[:mid]
            r = nums[mid:]
            return self.merge(self.sortArray(l), self.sortArray(r))

    def merge(self, l, r):
        out = []
        while l and r:
            if l[0] < r[0]:
                out.append(l.pop(0))
            else:
                out.append(r.pop(0))
        out += l
        out += r
        return out