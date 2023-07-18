# LRU Cache
class LRUCache:

    class Node:
        def __init__(self, key: int = -1, val: int = -1):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.map = {}
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        del self.map[node.key]
    
    def add(self, node: Node):
        currHead = self.head.next
        self.head.next = node
        currHead.prev = node
        node.prev = self.head
        node.next = currHead
        self.map[node.key] = node
    
    def removeLast(self):
        self.remove(self.tail.prev)

    def get(self, key: int) -> int: # O(1)
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None: # O(1)
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            self.add(node)
            node.val = value
        else:
            self.size += 1
            if self.size > self.cap:
                self.removeLast()
                self.size -= 1

            newNode = self.Node(key, value)
            self.add(newNode)
        