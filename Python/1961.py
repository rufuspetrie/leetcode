class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        # While words is a substring of s, add it to the word
        for i in range(len(words)):
            if words[i] in s and prefix != s:
                prefix += words[i]
            else:
                break
        
        return(prefix == s)