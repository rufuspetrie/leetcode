# First thoughts
    # Can start by doing binary search and finding midpoint of the first array
    # From there, find number less than this element in second array
    # Continue this process until the number of elements in the arrays equals half
    # This might be slow because for each binary search on one array, you will need
        # to do binary search again on the other way
# Better approach
    # For the median, we know that a fixed number of elements will be less than it
    # So, if we take subarrays from the first and second array,
        # and if we can form the subarray that would result from merging the arrays,
        # we know that the median will be the next element
    # Suppose that N is the number of elements that precedes the median
    # We take len(arr1)/2 elements from the first array and N - len(arr1)/2 from the second
    # Then, if all elements of subarr1 are less than the successor element to subarr2,
        # and all the elements of subarr2 are less than the next successor element to subarr1,
        # this is the subarray that would result from sorting the two sequences,
        # and we can let the next highest number equal the median
    # Our job then becomes picking partitions of the arrays such that the union of the
        # two subarrays equals the sorted merged array
    # We can find these partitions using binary search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        mid = N//2
        
        # Convention: pick indices from smaller array A
        A, B = nums1, nums2
        if len(B) < len(A): A, B = B, A

        l = 0
        r = len(A) - 1
        while True:
            i = (l + r)//2
            j = mid - i - 2

            A_l = A[i] if i >= 0 else float("-infinity")
            A_r = A[i+1] if i + 1 < len(A) else float("infinity")
            B_l = B[j] if j >= 0 else float("-infinity")
            B_r = B[j+1] if j + 1 < len(B) else float("infinity")

            if A_l <= B_r and B_l <= A_r:
                if N % 2 == 1:
                    return min(A_r, B_r)
                else:
                    return 0.5 * (max(A_l, B_l) + min(A_r, B_r))
            elif A_l > B_r:
                r = i - 1
            else:
                l = i + 1