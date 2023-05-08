# First guess at algorithm
    # Create counter for t
    # Create counter for t characters in s
    # Create r/l pointer
    # While the s counter has values less than the t counter, advance r
    # Once the substring has all characters, advance the left pointer
    # Repeat while r in range, shrink l pointer if possible
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for i in t:
            if i in count.keys(): count[i] += 1
            else: count[i] = 1

        window = {}
        l = 0
        have = 0
        need = len(count)
        interval = [-1, -1]
        min_len = float("inf")

        for r in range(len(s)):
            # Add character to window
            window[s[r]] = 1 + window.get(s[r], 0)
            # Check if it's a required character
            if s[r] in count and window[s[r]] == count[s[r]]: have += 1
            # Shrink window
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    interval = [l, r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]: have -= 1
                l += 1

        l, r = interval
        return s[l:r+1] if min_len != float("inf") else ""