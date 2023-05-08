# Similar to permutation but only need to permute alpha characters
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []

        def backtrack(ss = "", n = 0):
            # Letters exhausted - add permutations
            if len(ss) == len(s):
                permutations.append(ss)
            # If alphanumeric, swap current letter and call backtrack
            else:
                if s[n].isalpha():
                    backtrack(ss + s[n].swapcase(), n + 1)
                backtrack(ss + s[n], n + 1)

        backtrack()
        return permutations