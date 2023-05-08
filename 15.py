# Algorithm
    # Sort array to avoid duplicate solutions
    # Iterate through the array, fixing one value and doing 2sum on the resulting subarray
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, n in enumerate(nums):
            
            # don't reuse first element
            if i > 0 and n == nums[i-1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    cur_sum = n + nums[l] + nums[r]
                    if cur_sum < 0:
                        l += 1
                    elif cur_sum > 0:
                        r -= 1
                    else:
                        output.append([n, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1

        return output