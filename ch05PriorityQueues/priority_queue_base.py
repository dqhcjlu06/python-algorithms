from mybase.exceptions import EmptyError

class PriorityQueueBase:
    """优先队列基类"""

    # ---------- nested _Item class -----------
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            return self._key < other._key
        
        def __repr__(self):
            return '({0}, {1})'.format(self._key, self._value)
    
    # ------- public behaviors ----------------
    def is_empty(self):
        return len(self) == 0
    
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def add(self, key, value):
        raise NotImplementedError('must be implemented by subclass')

    def min(self):
        raise NotImplementedError('must be implemented by subclass')

    def remove_min(self):
        raise NotImplementedError('must be implemented by subclass')
