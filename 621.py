# Initial thoughts
    # want to prioritize more numerous elements - use max heap to select elements
    # to manage cooldown, can use a queue with size n
        # pop most numerous element from the heap and add it to the queue
        # after n units of time, pop from the queue and push to the heap
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        queue = deque()
        heap = [-i for i in c.values()]
        heapify(heap)

        time = 0
        while queue or heap:
            time += 1
            # Are there any elements to process?
            if heap: 
                count = heappop(heap) + 1
                if count:
                    queue.append((count, time + n))
            # Are any elements off cooldown?
            if queue and queue[0][1] == time: 
                heappush(heap, queue.popleft()[0])

        return time