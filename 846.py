# Initial thoughts
    # notice that there can be duplicate cards like in example 1,
        # so you can't just use a heap
    # need counter for the number of cards, heap to track rank
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False
        
        count = {}
        for i in hand:
            if i in count.keys(): count[i] += 1
            else: count[i] = 1

        heap = list(count.keys())
        heapify(heap)

        while heap:
            card = heap[0]
            for i in range(card, card + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                
                if count[i] == 0:
                    heappop(heap)

        return True