# Initial intuition/thoughts
    # Basically correct except going to use a doubly linked list instead of a queue
    # Because you can reuse elements already in the middle of a queue, need to be able to pop
        # from arbitrary indices and enqueue at the beginning, and idk if queues have
        # fast removal for randomly accessed elements, but LL's do if we have pointers in a hash
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}

        # Pointers for right (MRU) and left (LRU)
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # When inserting, MRU goes next to rightmost pointer (tail)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    # Can remove arbitrary nodes because need to remove/reinsert
        # queries that we perform multiple times to maintain LL order
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Remove/insert key to maintain order of LRU cache
    def get(self, key: int) -> int:
        if key in self.d.keys():
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].value
        else:
            return -1

    # Remove/insert key to maintain order of LRU cache
    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.remove(self.d[key])
        self.d[key] = Node(key, value)
        self.insert(self.d[key])

        # If over capacity, clear the node next to hear (LRU) of the linked list
        if len(self.d.keys()) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.d[LRU.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)