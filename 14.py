# Note
    # None of the official solutions used a trie, so may want to loop back later
        # and browse over the other solutions, probably can save some trouble
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        if word == "":
            cur.children[""] = TrieNode()

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.EOW = True

    def prefix(self) -> str:
        cur = self.root

        out = ""
        if len(cur.children) == 1:
            for char in cur.children:
                out += char
                cur = cur.children[char]

        while len(cur.children) == 1 and not cur.EOW:
            for char in cur.children:
                out += char
                cur = cur.children[char]
        return out
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = Trie()
        for i in strs: x.insert(i)
        x = x.prefix()
        return x