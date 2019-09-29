from .priority_queue_base import PriorityQueueBase
from ch03linked.positional_list import PositionalList
from mybase.exceptions import EmptyError

# 未排序优先级队列
# 操作                         运行时间
# len                            O(1)
# is_empty                       O(1)
# add                            O(1)
# min                            O(n)
# remove_min                     O(n)
class UnsortedPriorityQueue(PriorityQueueBase):
    
    # -------------------- nonpublic behavior --------------
    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise EmptyError('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    # -------------------- publict behaviors ----------------
    def __init__(self):
        """Create a new empty Priority Queue. """
        self._data = PositionalList()
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)