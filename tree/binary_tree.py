
from .tree import Tree

class BinaryTree(Tree):
    """ 二叉树 """

    # ----------------- additional abstract methods --------------
    def left(self, p):
        """ 返回左子树 """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ 返回右子树 """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """ 返回兄弟节点 """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    # 二叉树的中序遍历：对于每个位置p, p讲先访问左子树之后及其右子树之前被中序遍历访问
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield p

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
    # override inherited
    def positions(self):
        return self.inorder()