# 欧拉图
class EulerTour:
    """ Abstruct base class for performing Euler tour of a tree """
    def __init__(self, tree):
        self._tree = tree
    
    def tree(self):
        return self._tree
    
    def execute(self):
        if len(self._tree > 0):
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        p       Position of current node being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        return self._hook_postvisit(p, d, path, results)

    def _hook_previsit(self, p, d, path):
        """Visit Position p, before the tour of its children.
        p       Position of current position being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        """
        pass

    def _hook_postvisit(self, p, d, path, results):
        """Visit Position p, after the tour of its children.
        p       Position of current possition being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        results is a list of values returned by _hook_postvisit(c)
                for each child c of p
        """
        return results

class PreorderPrintIndexedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*'' + str(p.element()))

class BinaryEulerTour(EulerTour):
    """二叉树欧拉遍历
    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any)
    """
    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer


    def _hook_invisit(self, p, d, path):
        """Visit Position p, between tour of its left and right subtrees."""
        pass

# 二叉树图形布局的子类
# 每个位置p制定x坐标和y坐标
# x(p) p之前T的中遍历访问的位置数量
# y(p) T中p的深度
class BinaryLayout(BinaryEulerTour):
    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1
