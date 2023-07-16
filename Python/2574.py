class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        right_sums = []
        left_sums = []
        dif = []
        for i in range(len(nums)):
            left_sums.append(sum(nums[:i]))
            right_sums.append(sum(nums[i+1:]))
            dif.append(abs(left_sums[i]-right_sums[i]))
        return dif