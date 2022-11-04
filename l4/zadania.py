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

    def __init__(self, v: Any):
        self.root = TreeNode(v)

    #def add(self, value: Any, parent_name: Any) -> None:
        #w parametrze parent_value?
    
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)
    
    def for_each_deep_visit(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)
    
    #def show(self)


def vst_level(a: TreeNode):
    print(a)

def test_drzewo():
    a = Tree('F')
    a.root.add(TreeNode('B'))
    a.root.children[0].add(TreeNode('A'))
    a.root.children[0].add(TreeNode('D'))
    a.root.children[0].children[1].add(TreeNode('C'))
    a.root.children[0].children[1].add(TreeNode('E'))
    a.root.add(TreeNode('G'))
    a.root.children[1].add(TreeNode('I'))
    a.root.children[1].children[0].add(TreeNode('H'))
    print("Level order:")
    a.root.for_each_level_order(vst_level)
    print("Deep first:")
    a.root.for_each_deep_first(vst_level)

test_drzewo()