# Initial thoughts
    # Greedy approach could work
        # Choose first letter of string
        # Push end of partition to final incidence of that letter
        # Repeat this process for all letters in the partition
    # In particular,
        # Iterate through the string
        # Keep track of the greatest final incidence of each character
        # If current index equals the greatest, start a new substring
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        endpoint = 0
        idx = 0
        res = []

        for i, c in enumerate(s):
            idx = max(idx, last[c])
            if i == idx:
                res.append(i - endpoint + 1)
                endpoint = i + 1

        return res