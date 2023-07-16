# Every sequence ends with an increasing subsequence
# We can not make an increasing sequence larger by swapping elements
# Search until we find an area where the 
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        # Find first nonincreasing element at end of permutation
        if len(arr) < 2: return arr
        idx = -1
        for i in range(len(arr) - 1, 0, -1):
            if arr[i-1] > arr[i]:
                idx = i - 1
                break

        # If it's all increasing, it's already the smallest
        if idx == -1:
            return arr

        # Find largest element less than arr[idx] in the tail
        idy = idx + 1
        for i in range(idx + 1, len(arr)):
            if arr[i] < arr[idx] and arr[i] > arr[idy]:
                idy = i

        # Swap and return
        arr[idx], arr[idy] = arr[idy], arr[idx]
        return arr