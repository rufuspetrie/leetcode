# Initial thoughts
    # When looking at the different input words, can just compare the first
        # characters until you find a difference
    # From that difference, can work out a lexical ordering
    # Can determine the lexical ordering of the language by finding a 
        # topological sort of the character orders
class Solution:
    def alien_order(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w1 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[i]:
                    graph[w1[j].add(w2[j])]
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True

            for neighbor in graph[char]:
                if dfs(neighbor):
                    return True
                
            visited[char] = False
            res.append(char)

        for char in graph:
            if dfs(char):
                return ""
            
        res.reverse()
        return "".join(res)