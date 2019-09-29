class _DoublyLinkedBase:
    """双向链表基类"""
    # ----------- nested _Node class ---------------
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._prev = self._header
        self._size = 0

    # ------------------ public accessors ----------------
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    # ------------------ nonpublic utilities -------------
    def _insert_between(self, e, predecessor, sucessor):
        newest = self._Node(e, predecessor, sucessor)
        predecessor._next = newest
        sucessor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None # 删除node
        return element
    
