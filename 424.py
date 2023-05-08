# Initial thoughts
    # Want to find the longest substring such that all characters but k are equal
    # Set won't work for this because it doesn't account for multiplicity of elements
    # So, need to keep hash of characters in current substring
    # In particular, keep track of the count of the most frequent character
    # If len(subarray) - count(most_frequent) <= k, then it's a valid substring
# Note
    # Do not need to scan for max frequency at each step, only check if the frequency
        # of the current character is greater than the max_frequency
    # This is because the max len will be maximized whenever there is a new max frequency,
        # so only need accurate counts when we're at a new highest value
# Note
    # counts.get(s[r], 0) will try to get a key-value and return 0 if it doesn't exist
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_len = 0
        l = 0
        r = 0
        max_freq = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_freq = max(max_freq, counts[s[r]])
            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return  max_len