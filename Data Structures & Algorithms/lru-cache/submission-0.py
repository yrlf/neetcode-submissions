class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.right = self.tail
        self.tail.left = self.head
        self.record = {}

    def _remove(self, node:Node):
        node.left.right = node.right
        node.right.left = node.left
        return node


    def _insertLast(self, node:Node):
        node.left = self.tail.left
        node.right = self.tail
        self.tail.left.right = node
        self.tail.left = node

    def get(self, key: int) -> int:
        if key not in self.record:
            return -1
        
        node = self.record[key]
        self._remove(node)
        self._insertLast(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.record:
            node = self.record[key]
            node.val = value
            self.get(key)
        else:
            if len(self.record) == self.capacity:
                oldNode = self._remove(self.head.right)
                del(self.record[oldNode.key])
            newNode = Node(key, value)
            self.record[key] = newNode
            self._insertLast(newNode)
    

