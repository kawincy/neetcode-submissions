class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.LRUheap = []
        self.clock = 0

    def get(self, key: int) -> int:
        self.clock += 1
        if key in self.hashmap:
            value = self.hashmap[key][1]
            self.hashmap[key] = (self.clock, value)
            heapq.heappush(self.LRUheap, (self.clock, key))
            return value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        self.clock += 1
        self.hashmap[key] = (self.clock, value)
        heapq.heappush(self.LRUheap, (self.clock, key))

        while len(self.hashmap) > self.capacity:
            popped = heapq.heappop(self.LRUheap)
            if popped[0] == self.hashmap[popped[1]][0]:
                self.hashmap.pop(popped[1])
            




