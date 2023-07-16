# Notes
    # For this problem, it's easier just to think how the array becomes two increasing subarrays
        # with an inflection point potentially on different sides of mid
    # If coded correctly, this approach generalizes to situations where the subarrays aren't
        # rotated, and it requires significantly less code
    # The video you watched on this was garbage so just come back and whiteboard this again
        # with a clear head
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid            
            
            # Inflection point left of mid
            if nums[r] > nums[mid]:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
        return -1