# Initial thoughts
    # use graph to represent word transformations
    # in particular, insert a "*" into all positions in the word so that
        # we can easily match it
        # e.g. hot and dot will both have *ot, so they share an edge
        # graph will have form {*ot: [mapped words]}
    # should probably use BFS for traversal to find min
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.append(beginWord)

        # Map words to all possible wildcard versions
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i+1:]
                graph[wildcard].append(word)

        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        
        # BFS: for each word in queue, generate its wildcards
        distance = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord: return distance
                for j in range(len(word)):
                    wildcard = word[:j] + "*" + word[j+1:]
                    for w in graph[wildcard]:
                        if w not in visited:
                            visited.add(w)
                            queue.append(w)
            distance += 1

        return 0