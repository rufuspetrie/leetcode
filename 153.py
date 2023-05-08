# Initial thoughts
    # After rotating the array, it either stays the same or becomes two increasing arrays
    # If the array has been rotated, L[0] > L[-1] beacuse it's the next highest rank
    # Example: [4,5,6,7,0,1,2]
        # L[0] < L[-1], so we know the array is rotated
        # L[m] = 7 > L[l] = 4
        # Because the array is rotated, it is made up of two increasing subarrays
        # L[:m+1] increases and lower elements are in L[m+1:], so the minimum
            # has to be in the second half of the search space
        # So, let l = mid + 1 and continue this logic
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        cur_min = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(cur_min, nums[l])
                
            mid = (l + r)//2
            cur_min = min(cur_min, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return cur_min