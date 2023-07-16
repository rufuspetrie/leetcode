class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        out = []
        for i in nums1:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for i in nums2:
            if i in d.keys() and d[i] > 0:
                out.append(i)
                d[i] -= 1
        
        return out