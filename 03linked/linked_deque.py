from .doubly_linked_base import _DoublyLinkedBase
from mybase.exceptions import EmptyError

class LinkedDeque(_DoublyLinkedBase):
    
    def first(self):
        if self.is_empty():
            raise EmptyError('Dequeue is empty')
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise EmptyError('Dequeue is empty')
        return self._tailer._prev._element
    
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        self._insert_between(e, self._tailer._prev, self._tailer)
    
    def delete_first(self):
        if self.is_empty():
            raise EmptyError('Dequeue is empty')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise EmptyError('Dequeue is empty')
        return self._delete_node(self._tailer._prev)
