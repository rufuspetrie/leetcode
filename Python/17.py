# Algorithm
    # Very similar to permutation generator
    # Instead of iterating through each remaining number for each index,
        # iterate through the available letters for that index
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "": return []
        nums = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.string = ""
        perms = []
        max_len = len(digits)

        def perm(n = 0):
            if len(self.string) == max_len:
                perms.append(self.string)
            else:
                for i in nums[digits[n]]:
                    self.string += i
                    perm(n + 1)
                    self.string = self.string[:len(self.string)-1]
        
        perm()
        return perms