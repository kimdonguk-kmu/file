from btree_builder import BTreeBuilder
from queues import Queue
from tree_node import TreeNode
import copy



class BTree:
    def __init__(self, root):
        self.root = root

    def search_dfs(self, elem):
        ret = None

        def dfs_recursive_preorder(root):
            nonlocal ret

            if root is None:
                return

            if root.elem == elem:
                ret = root
                return

            dfs_recursive_preorder(root.left_child)
            dfs_recursive_preorder(root.right_child)

        def dfs_recursive_postorder(root):
            nonlocal ret

            if root is None:
                return

            dfs_recursive_postorder(root.left_child)
            dfs_recursive_postorder(root.right_child)
            if root.elem == elem:
                ret = root
                return

        def dfs_recursive_inorder(root):
            nonlocal ret

            if root is None:
                return

            dfs_recursive_inorder(root.left_child)
            if root.elem == elem:
                ret = root
                return
            dfs_recursive_inorder(root.right_child)


        dfs_recursive_preorder(self.root)
        return ret

    def search_bfs(self, elem):
        if self.root is None:
            return None

        ret = None
        queue = Queue()

        root = self.root
        queue.enque(root)

        while queue.peek().elem != elem and not queue.is_empty:
            root = queue.peek()
            queue.dequeue()

            if root.left_child is not None:
                queue.enqueue(root.left_child)

            if root.left_child is not None:
                queue.enqueue(root.left_child)

        ret = None if queue.isempty() else queue.peek()

        return ret

    def copy(self):
        def copy_recursive(root):
            if root is None:
                return

            node = TreeNode(root.elem)
            node.left_child = copy_recursive(root.left_child)
            node.right_child = copy_recursive(root.right_child)
            return node

        return BTree(copy_recursive(self.root))

    def copy_builtin(self):
        return copy.deepcopy(self)

    def traverse_postorder(self):
        ret = []

        # using recursive

        def postorder_recursive(root):
            if root is None:
                return

            postorder_recursive(root.left_child)
            postorder_recursive(root.right_child)
            ret.append(root)

        postorder_recursive(self.root)

        return ret


if __name__ == "__main__":
    sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = BTree(root)
    tree1 = tree.copy()
    tree2 = tree.copy_builtin()
    tree3 = tree
    tree.root.left_child.right_child.elem = "Z"
    actions = tree.traverse_postorder()
    print(actions)
    actions = tree1.traverse_postorder()
    print(actions)
    tree1.root.left_child.right_child.elem = "W"
    actions = tree1.traverse_postorder()
    print(actions)
    actions = tree2.traverse_postorder()
    print(actions)
    actions = tree3.traverse_postorder()
    print(actions)