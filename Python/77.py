# How is this different from the permutation algorithm?
    # Here, we need to creat a subset of the numbers instead of working in place
    # Furthermore, we need to avoid creating duplicate permutations of the same group
    # We do this by starting the loop range one higher each time
    # This means that combinations starting with 2 will hever have 1 and so on
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def combine(low = 1, combination = []):
            if len(combination) == k:
                combinations.append(combination[:])
            else:
                for i in range(low, n + 1):
                    combination.append(i)
                    combine(i + 1, combination)
                    combination.pop()

        combine()
        return combinations