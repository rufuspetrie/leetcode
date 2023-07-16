# Initial thoughts
    # Think of drawing decision tree with all possible partitions
        # In each possible layer, choose a partition and see if it's a palindrome
        # If so, generate another layer for the remaining letters and repeat
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []

        def dfs(idx = 0, partition = []):
            if idx >= len(s):
                partitions.append(partition[:])
            else:
                for i in range(idx, len(s)):
                    if s[idx:i+1] == s[idx:i+1][::-1]:
                        partition.append(s[idx:i+1])
                        dfs(i+1, partition)
                        partition.pop()

        dfs()
        return partitions