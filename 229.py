class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        k = floor(len(nums)/3)
        c = [i for i in c.keys() if c[i] > k]
        return c