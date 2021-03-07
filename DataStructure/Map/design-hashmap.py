# question link: https://leetcode.com/problems/design-hashmap/

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.m = 1009
        self.data = [None] * self.m
        

    def put(self, key: int, value: int) -> None:
        modula = key % 1009
        if not self.data[modula]:
            self.data[modula] = Node(key, value)
            return
        cur = self.data[modula]
        prev = None
        while cur:
            if cur.key == key:
                cur.val = value
                return
            else:
                prev = cur
                cur = cur.next
        prev.next = Node(key, value)

    def get(self, key: int) -> int:
        cur = self.data[key % 1009]
        while cur:
            if cur.key == key:
                return cur.val
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        modula = key % 1009
        cur = self.data[modula]
        if not cur:
            return
        if cur.key == key:
            self.data[modula] = cur.next
            return
        prev = cur
        cur = cur.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
