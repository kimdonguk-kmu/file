from propositional_tree import TreeNode
from stacks import Stack

class BTreeBuilder:

    @staticmethod
    def build(sexpr):
        stack = Stack()

        it = iter(sexpr)
        root = None

        while stack.is_empty() or it:
            try:
                token = next(it)
            except StopIteration:
                break

            if token != ")":
                if token == "#":
                    stack.push(TreeNode(None))
                else:
                    stack.push(TreeNode(token))
                continue

            stack_ = Stack()
            while stack.peek().elem != "(":
                stack_.push(stack.peek())
                stack.pop()

            stack.pop()

            if stack.is_empty():
                root = stack_.peek()
                break
            node = stack.peek()

            if stack_.peek() != TreeNode(None):
                node.left_child = stack_.peek()
            stack_.pop()
            if stack_.peek() != TreeNode(None):
                node.right_child = stack_.peek()
            stack_.pop()

            if stack.is_empty():
                root = node
                continue

            # root = stack.peek()
            # root.left_child = prev
            # stack.pop()
            # stack.push(root)

        if not stack.is_empty():
            raise Exception("expression is wrong.")

        return root