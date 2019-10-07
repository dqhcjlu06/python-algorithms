from ch04tree.linked_binary_tree import LinkedBinaryTree
from ch06Maps.map_base import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree. """

    # ----------------- override Position class --------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
        
        def value(self):
            return self.element()._value()
    
    # ------------------- nonpublic utilities -------------------
    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p
    
    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p. """
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk
    
    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk
    
    # ------------ public methods providing "positional" support ----------------
    def first(self):
        """Return the first Position in the tree"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    
    def last(self):
        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    
    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def after(self, p):
        """Return the position just after p in the natural order.

        Return None if p is the last position
        """
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def find_position(self, k):
        """Return position with key k, or else neighbor"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p
    
    def delete(self, p):
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)
    
    # -------------- public methods for (standard) map interface ----------------
    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    
    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k,v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)
    
    def __delitem__(self, k):
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    def __iter__(self):
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    # -------------- public methods for sorted map interface -----------------
    def __reversed__(self):
        p = self.last()
        while p is not None:
            yield p.key()
            p = self.before(p)
    
    def find_min(self):
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())
    
    def find_max(self):
        if self.is_empty():
            return None
        else:
            p = self.last()
            return (p.key(), p.value())
    
    def find_le(self, k):
        if self.is_empty():
            return None
        else: 
            p = self.find_position(k)
            if k < p.key():
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None
    
    def find_lt(self, k):
        if self.is_empty():
            return None
        else: 
            p = self.find_position(k)
            if k < p.key():
                p = self.before(p)
            return (p.key(), p.value()) if p is not None else None
    
    def find_ge(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    
    def find_gt(self, k):
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if not p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None
    
    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    # -------------- hooks used by subclass to balance a tree ---------------
    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass

    def _rebalance_access(self, p):
        pass

    # -------- nonpublic methods to support tree balancing -----------------
    
    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)"""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent
    
    def _rotate(self, p):
        #Rotate Position p above its parent
        # Switches between these configurations, depending on whether p==a or p==b.

        #      b                  a
        #     / \                /  \
        #    a  t2             t0   b
        #   / \                     / \
        #  t0  t1                  t1  t2

        # Caller should ensure that p is not the root.
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        # now rotate x and y, including transfer of middle subtree
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True)
    
    def _restructure(self, x):
        # Perform a trinode restructure among Position x, its parent, and its grandparent.

        # Return the Position that becomes root of the restructured subtree.

        # Assumes the nodes are in one of the following configurations:

        #     z=a                 z=c           z=a               z=c  
        #    /  \                /  \          /  \              /  \  
        #   t0  y=b             y=b  t3       t0   y=c          y=a  t3 
        #      /  \            /  \               /  \         /  \     
        #     t1  x=c         x=a  t2            x=b  t3      t0   x=b    
        #        /  \        /  \               /  \              /  \    
        #       t2  t3      t0  t1             t1  t2            t1  t2   

        # The subtree will be restructured so that the node with key b becomes its root.

        #          b
        #        /   \
        #      a       c
        #     / \     / \
        #    t0  t1  t2  t3

        # Caller should ensure that x has a grandparent.
        # Perform trinode restructure of Position x with parent/grandparent
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x
    