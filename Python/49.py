# Notes
    # sorting is slow, so want to use a hash
    # can't use Counter() for hash keys because they're mutable
    # instead, create tuple version of counter by making list of char counts
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord("a")] += 1
            d[tuple(count)].append(word)

        return list(d.values())