# Initial thoughts
    # Can probably do DFS, but need ability to visit nodes multiple times
    # Need to sort adjacency list, perform DFS in lexical order because
        # the return itinerary needs to be the lowest lexical one
    # We know the search is complete if len(itinerary) == len(tickets) + 1
        # because we start at a node and traverse len(tickets) edges
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = ["JFK"]
        tickets.sort()
        graph = {i: deque() for i, j in tickets}
        for i, j in tickets:
            graph[i].append(j)

        def dfs(node):
            if len(itinerary) == len(tickets) + 1:
                return itinerary
            if node not in graph:
                return False
            
            # Note: need separate list for graph[node] because we can't
                # iterate over it and mutate it at the same time
            temp = list(graph[node])
            for n in temp:
                graph[node].popleft()
                itinerary.append(n)
                if dfs(n):
                    return itinerary
                itinerary.pop()
                graph[node].append(n)
            
            return False
        
        return dfs(itinerary[0])