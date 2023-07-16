# Initial thoughts
    # Similar to other backtracking problems, use an inclusion/exclusion scheme
    # Unlike first combination problem, need to advance pointer after using element
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def dfs(idx = 0, cur_sum = 0, elements = []):
            if cur_sum == target:
                combinations.append(elements[:])
                idx += 1
            elif cur_sum > target:
                idx += 1
            elif idx == len(candidates):
                return
            else:
                # Include element at idx
                cur_sum += candidates[idx]
                elements.append(candidates[idx])
                dfs(idx + 1, cur_sum, elements)

                # Don't include element at idx
                cur_sum -= candidates[idx]
                elements.pop()
                dfs(idx + 1, cur_sum, elements)

        dfs()
        return combinations