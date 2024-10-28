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
        

# 
class Node:
    def __init__(self):
        pass
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.root = Node()
        self.end = Node()
        self.root.next = self.end
        self.end.prev = self.root
        self.memo = {}

    def get(self, key: int) -> int:
        if key in self.memo:
            node = self.memo[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del self.memo[node.key]

    def add(self, node):
        temp = self.root.next
        self.root.next = node
        node.prev = self.root
        node.next = temp
        temp.prev = node
        self.memo[node.key] = node

    def removeLast(self):
        lastNode = self.end.prev
        self.remove(lastNode)

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            node = self.memo[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node()
            node.val = value
            node.key = key
            
            self.add(node)
            if len(self.memo) > self.size:
                self.removeLast()

# one root
class Node:
    def __init__(self, key: int=0, val: int=0):
        self.next = None
        self.val = val
        self.prev = None
        self.key = key
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.memo = {}

    def get(self, key: int) -> int:
        if key not in self.memo:
            return -1
        node = self.memo[key]
        self.remove(node)
        self.add(node)
        return node.val

    def add(self, node):
        head = self.root.next
        node.next = head
        head.prev = node
        self.root.next = node
        node.prev = self.root

    def remove(self, node):
        temp_next = node.next
        temp_prev = node.prev
        temp_prev.next = temp_next
        temp_next.prev = temp_prev


    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            node = self.memo[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.memo) == self.capacity:
                last_node = self.root.prev
                del self.memo[last_node.key]
                self.remove(last_node)
            new_node = Node(key, value)
            self.add(new_node)
            self.memo[key] = new_node