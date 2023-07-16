class Solution:
    def partitionString(self, s: str) -> int:
        cache = set()
        parts = 1
        for i in s:
            if i in cache:
                cache = set()
                parts += 1
            cache.add(i)

        return parts