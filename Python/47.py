# Note
    # Same as 46, just check if dupe before adding to output
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        def perm(x = 0):

            if x == n:
                if nums[:] not in permutations:
                    permutations.append(nums[:])
            for i in range(x,n):
                nums[i], nums[x] = nums[x], nums[i]
                perm(x+1)
                nums[i], nums[x] = nums[x], nums[i]

        perm()
        return permutations