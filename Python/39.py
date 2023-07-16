# Initial thoughts
    # Think in terms of an inclusion/exclusion tree
    # Unlike before, can repeatedly include elements until the new
        # array sum is greater than the target
    # Need DFS function to take index, cur_sum, element list as arguments
# New tree:
    # Think of the decision tree as splitting on the inclusion/exclusion of elements
    # Unlike the combination one, can repeat the choice to include elements
    # For example, going down the left nodes of the trees for the example
        # results in repeatedly adding 2s to the sum
    # After the base case is reached, start taking right paths to include new elements
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx = 0, cur_sum = 0, elements = []):
            if cur_sum == target:
                result.append(elements[:])
                idx += 1
            elif cur_sum > target:
                idx += 1
            elif idx == len(candidates):
                return
            else:
                # Include current element
                cur_sum += candidates[idx]
                elements.append(candidates[idx])
                dfs(idx, cur_sum, elements)
                
                # Don't include current element
                cur_sum -= candidates[idx]
                elements.pop()
                dfs(idx + 1, cur_sum, elements)

        dfs()
        return result