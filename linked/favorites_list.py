# 利用PositionalList类作为存储辅助实现一个收藏夹列表
# 按照访问次数的降序来存储这些元素

from .positional_list import PositionalList

class FavoritesList:
    
    # ------------- neted _Item class -------------
    class _Item:
        __slots__ = '_value', '_count'  # 存储使用次数

        def __init__(self, e):
            self._value = e
            self._count = 0
    
    # -------------- nonpublic utilities -------------
    def _find_position(self, e):
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self, p):
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                        cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    # -------------- public methods ------------------
    def __init__(self):
        self._data = PositionalList()
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def access(self, e):
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)
    
    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    # 获取访问量k个    
    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        j = 0
        while j < k:
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
            j += 1
    
    def __repr__(self):
        return ','.join('{0}:{1}'.format(i._value, i._count) for i in self._data)

if __name__ == "__main__":
    fav = FavoritesList()
    for c in 'hello. this is a test of':
        fav.access(c)
        k = min(5, len(fav))
        print('Top {0})'.format(k))