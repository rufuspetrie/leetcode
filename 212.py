# Initial thoughts
    # Similar to first word search problem except need to search for multiple words
    # To cut down on the amount of searching, generate a trie containing the search words
    # At each stage in the DFS, only continue searching if a neighboring cell has
        # a child of the current trie node
    # Iterate through grid and start the search at each cell
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False
        self.refs = 0

    def insert(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children.keys():
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.EOW = True

    def delete(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words: root.insert(w)
        
        rows = len(board)
        cols = len(board[0])
        result = set()
        visited = set()

        def dfs(r, c, node, word):
            if(
                r not in range(rows)
                or c not in range(cols)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r,c) in visited
            ):
                return
                
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.EOW: 
                node.EOW = False
                result.add(word)
                root.delete(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)