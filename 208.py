# Naive code
    # Originally used a dictionary
    # This could check inclusion fast but had to search through all keys for prefixes
# Improvement
    # Have nodes as each entry in the prefix tree
    # Each node has a hash set that contains its children (also nodes)
    # Each node also has an EOF bool that signifies whether it's a word or not
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.EOW = True

    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        
        if cur.EOW:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for char in prefix:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        
        return True