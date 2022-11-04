from typing import Any, Callable, List, Union
from dane import Queue

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, v: Any):
        self.value = v
        self.children = []

    def is_leaf(self) -> bool:
        return len(self.children) > 0
    
    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)
        
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        nq = Queue()
        for x in self.children:
            nq.enqueue(x)
        while len(nq) > 0:
            nqe: TreeNode = nq.dequeue()
            visit(nqe)
            for y in nqe.children:
                nq.enqueue(y)
    
    #def search(value: Any) -> Union['TreeNode', None]:
        #nie rozumiem
    
    def __str__(self):
        return str(self.value)

class Tree:
    root: TreeNode

    def __init__(self):
        root = TreeNode()

    #def add(self, value: Any, parent_name: Any) -> None:
        #w parametrze parent value?
    
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)
    
    def for_each_deep_visit(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)
    
    #def show(self)


def test_drzewo():
    a = Tree()
    a.root.add(TreeNode('F'))
    a.root.children[0].add('B')
    a.root.children[0][0].add('A')
    a.root.children[0][0].add('D')
    a.root.children[0][0][1].add('C')
    a.root.children[0][0][1].add('E')
    a.root.children[0].add('G')
    a.root.children[0][1].add('I')
    a.root.children[0][1][0].add('H')