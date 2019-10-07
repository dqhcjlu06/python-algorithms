from ch03linked.positional_list import PositionalList
from ch03linked.favorites_list import FavoritesList

# 位置列表执行插入排序
def insertion_sort(L):
    if (len(L) > 1):
        maker = L.first()
        while maker != L.last():
            pivot = L.after(maker)
            value = pivot.element()
            if value > maker.element():
                maker = pivot
            else:
                walk = maker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

if __name__ == "__main__":
    L = PositionalList()
    L.add_first(2)
    L.add_first(5)
    L.add_first(9)
    L.add_first(7)
    L.add_first(4)
    L.add_first(6)
    insertion_sort(L)
    print('PositionalList {0}'.format([e for e in L]))

    fav = FavoritesList()
    for c in 'hello. this is a test of':
        if c  != ' ':
            fav.access(c)
            k = min(5, len(fav))
            print('Top {0}) {1} {2}'.format(k, [x for x in fav.top(k)], fav))
    