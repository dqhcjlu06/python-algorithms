from .priority_queue_base import PriorityQueueBase
from ch03linked.positional_list import PositionalList
from mybase.exceptions import EmptyError

# 排序优先队列实现
# 操作                运行时间
# len                   O(1)
# is_empty              O(1)
# add                   O(n)
# min                   O(1)
# remove_min            O(1)
class SortedPriorityQueue(PriorityQueueBase):

    # --------------- public behaviors -----------------
    def __init__(self):
        self._data = PositionalList()
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)
    
    def min(self):
        if self.is_empty():
            raise EmptyError('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise EmptyError('Priority queue us empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
