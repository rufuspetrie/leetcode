# Initial thoughts
    # Could sort intervals by startpoint and queries and try to process
        # in order somehow
    # Could alternately sort intervals by length and just check whether
        # each query falls in the interval
    # Better idea: just sort them both, push intervals onto stack by length
        # while they're valid and return the eventual minimum
        # can also keep track of the interval endpoint so you can pop from
            # the stack when processing the next query if necessary and add
            # new intervals that overlap the query
    # Note: can't sort the queries object because they need to be returned
        # in order, so iterate over the sorted version
    # Note: can just push intervals with l < q onto the stack and get rid of
        # them later instead of including multiple conditions
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        res = {}

        idx = 0
        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                l, r = intervals[idx]
                heapq.heappush(heap, (r - l + 1, r))
                idx += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[q] = heap[0][0]
            else:
                res[q] = -1

        return [res[q] for q in queries]