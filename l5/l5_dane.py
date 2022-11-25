from typing import *
import graphviz

class BinaryNode:

    def __init__(self, val: Any):
        self.value: Any = val
        self.left_child: 'BinaryNode' = None
        self.right_child: 'BinaryNode' = None
    
    def is_leaf(self) -> bool:
        return self.left_child is None and self.right_child is None

    def add_left_child(self, value: Any) -> None:
        if self.left_child is not None:
            raise ValueError("Left child już istnieje")
        self.left_child = BinaryNode(value)    
    
    def add_right_child(self, value: Any) -> None:
        if self.right_child is not None:
            raise ValueError("Right child już istnieje")
        self.right_child = BinaryNode(value)

    def __trav_l(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            visit(self.left_child.value)
    
    def __trav_this(self, visit: Callable[[Any], None]):
        visit(self.value)
    
    def __trav_r(self, visit: Callable[[Any], None]):
        if self.right_child is not None:
            visit(self.right_child.value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.__trav_l(visit)
        self.__trav_this(visit)
        self.__trav_r(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.__trav_l(visit)
        self.__trav_r(visit)
        self.__trav_this(visit)
    
    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.__trav_this(visit)
        self.__trav_l(visit)
        self.__trav_r(visit)

    def generate_graphviz_edges(self, g: graphviz.Graph) -> None:
        if self.left_child is not None:
            g.edge(str(self.value), str(self.left_child.value))
            self.left_child.generate_graphviz_edges(g)
        if self.right_child is not None:
            g.edge(str(self.value), str(self.right_child.value))
            self.right_child.generate_graphviz_edges(g)


    def __str__(self):
        return f'{self.value}'

class BinaryTree:

    def __init__(self, value: Any):
        self.root = BinaryNode(value)
    
    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)
        
    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)
        
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        g = graphviz.Graph('BinaryTree')
        self.root.generate_graphviz_edges(g)
        g.render('BinaryTree', view = True)


def test_tree():
    tree = BinaryTree(10)
    tree.root.add_left_child(9)
    tree.root.left_child.add_left_child(1)
    tree.root.left_child.add_right_child(3)

    tree.root.add_right_child(2)
    tree.root.right_child.add_left_child(4)
    tree.root.right_child.add_right_child(6)

    assert tree.root.value == 10

    assert tree.root.right_child.value == 2
    assert tree.root.right_child.is_leaf() is False
    
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.left_child.is_leaf() is True

    print("test_tree pass")
    tree.show()

if __name__ == "__main__":
    test_tree()