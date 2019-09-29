# Move-to-Front 启发式动态调整列表
# 启发式算法： 每访问一个元素， 都会吧该元素移动到列表的最前面

from .favorites_list import FavoritesList
from .positional_list import PositionalList

class FavoritesListMTF(FavoritesList):

    # override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))
    
    # override top because list is no longer sorted
    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        temp = PositionalList()

        # making a copy of the original list
        for item in self._data:
            temp.add_last(item)
        
        j = 0
        while j < k:
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)
            j += 1
