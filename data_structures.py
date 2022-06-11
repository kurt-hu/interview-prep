from collections import deque
import heapq

#=============================================
#==               Queue (FIFO)              ==
#=============================================
queue = deque()

# add item to queue
queue.append(10)
# remove item from queue
queue.popleft()
# remove all items from queue
queue.clear()

# Docs: https://docs.python.org/3/library/collections.html#collections.deque

#=============================================
#==              Stack (LIFO)               ==
#=============================================
stack = deque()

# push item to stack
stack.append(10)
# remove item from stack
stack.pop()
# remove all items from stack
stack.clear()

# Docs: https://docs.python.org/3/library/collections.html#collections.deque

#=============================================
#==         Heap (min priority queue)       ==
#=============================================

heap = []

# Push the value item onto the heap, maintaining the heap invariant.
heapq.heappush(heap, 5)
# Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
heapq.heappop(heap)
# Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
heapq.heappushpop(heap, 3)
# Transform list x into a heap, in-place, in linear time.
x = [3, 6, 2, -4]
heapq.heapify(x) # x = [-4, 3, 2, 6]

# Note: for max-heap, negate all values
# Docs: https://docs.python.org/3/library/heapq.html

#=============================================
#==            Trie (Prefix tree)           ==
#=============================================
class Trie():
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        
        curr['end'] = True
    
    def search(self, word):
        curr = self.root

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        
        return 'end' in curr
    
    def startsWith(self, word):
        curr = self.root

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        
        return True

#=============================================
#==               Union Find                ==
#=============================================

#TODO