# Initial thought: use Trie
    # Not sure how search will work with the dots though
    # Probably some type of DFS?
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.EOW = True

    def search(self, word: str) -> bool:

        def dfs(idx, root):
            cur = root
            for i in range(idx, len(word)):
                char = word[i]

                # Wildcard case - recursively call DFS on children nodes
                if char == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                # Regular character - keep iterating
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
            
            # If the word has survived checks, check EOW
            return cur.EOW

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)