from linked.linked_queue import LinkedQueue
import collections

# 抽象数据结构
class Tree:
    
    # ---------------- nested Position class ---------
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)
    
    # ------------------ abstract methods that concrete subclass must support -----
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implented by subclass')

    # -------- concrete methods implented in this class ------
    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))
    
    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p in None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.preorder()
    
    # 先序遍历：首先访问树的根，然后递归访问子树的根， 
    # 如果这颗树是有序的， 则根据孩子的顺序遍历子树
    def preorder(self):
        if not self.is_empty():
            for p in self._substree_preorder(self.root()):
                yield p

    def _substree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._substree_preorder(c):
                yield other
    
    # 优先遍历孩子的根，然后访问根
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    # 广度优先遍历：在访问树的深度d的位置之前，先访问深度d+1的位置
    def breadthfist(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.denqueue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)
    
    # 深度优先: 先访问分支路径深入到不能再深入为止 而且每个节点只能访问一次
    def depthfist(self):
        return self.preorder()