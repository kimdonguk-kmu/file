from btree_builder import BTreeBuilder


class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.value = None  # boolean value
        self.left_child = self.right_child = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"

class PropositionalTree:
    def __init__(self, root):
        self.root = root


    def calculate_propositional(self, *param):
        ret = None
        lst = param

        def calculate_recursive(root):
            if root is None:
                return

            if root.elem.isdigit():
                root.value = lst[root.elem]

        calculate_recursive(self.root)
        return ret


if __name__ == "__main__":
    sexpr = "( OR ( OR ( AND ( 0 NOT ( # 1 ) ) AND ( NOT ( # 0 ) 2 ) ) NOT ( # 2 ) ) )".split()
    root = BTreeBuilder.build(sexpr)
    tree = PropositionalTree(root)
    prop = tree.calculate_propositional(False, True, False)
    print(prop.value)