# Initial thoughts
    # A triplet with any value greater than the target values is no good
    # Among these triplets, need to find ones with equal value to a target
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = []
        for i, j, k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            else:
                candidates.append([i, j, k])

        res = [0, 0, 0]
        for i, j, k in candidates:
            if i == target[0]:
                res[0] = 1
            if j == target[1]:
                res[1] = 1
            if k == target[2]:
                res[2] = 1

        return sum(res) == 3