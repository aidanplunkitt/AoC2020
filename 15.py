STARTING = [0,3,6]

class LRU_Cache:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head, self.tail = self.Node(None), self.Node(None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.map = {}

    def __repr__(self):
        nodes = ["dh"]
        n = self.head.next
        while n is not self.tail:
            nodes.append(str(n.data))
            n = n.next
        nodes.append("dt")
        return " -> ".join(nodes)

    def insert(self, data):
        age = 0
        if data in self.map:
            n = self.map[data]

            # TODO make this O(1) time
            p = self.tail
            while p is not n:
                p = p.prev
                age += 1

            # remove from cache
            n.prev.next, n.next.prev = n.next, n.prev
        else:
            n = self.Node(data)
            self.map[data] = n

        # place in cache
        n.prev, n.next = self.tail.prev, self.tail
        self.tail.prev.next = n
        self.tail.prev = n

        return age

lc = LRU_Cache()
last = -1
nth_spoken = 1
for n in STARTING:
    last = lc.insert(n)
    nth_spoken += 1

for i in range(2020 - len(STARTING) - 1):
    last = lc.insert(last)
    nth_spoken += 1

print(nth_spoken, last)