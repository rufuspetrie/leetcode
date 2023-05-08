class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z_count = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z_count += 1
            else:
                nums[idx] = nums[i]
                idx += 1
        for i in range(idx, idx + z_count):
            nums[i] = 0
        print(nums)