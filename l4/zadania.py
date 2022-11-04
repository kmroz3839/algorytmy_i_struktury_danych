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
    
    def search_helper(self, a: 'TreeNode', value: Any, res: List['TreeNode']):
        if a.value == value:
            res[0] = a
            return
        else:
            for x in a.children:
                self.search_helper(x, value, res)
                if res[0] is not None:
                    return


    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        res = [None]
        for x in self.children:
            self.search_helper(x, value, res)
            if res[0] is not None:
                return res[0]
        return None
    
    def __str__(self):
        return str(self.value)

class Tree:
    root: TreeNode

    def __init__(self, v: Any):
        self.root = TreeNode(v)

    def add(self, value: Any, parent_name: Any) -> None:
        s: 'TreeNode' = self.root.search(parent_name)
        if s is None:
            raise ValueError("Nie znaleziono")
        else:
            s.add(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)
    
    def for_each_deep_visit(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)
    
    #def show(self)


def vst_print(a: TreeNode):
    print(a)

def test_drzewo():
    a = Tree('F')
    a.add('B', 'F')
    a.add('A', 'B')
    a.add('D', 'B')
    a.add('C', 'D')
    a.add('E', 'D')
    a.add('G', 'F')
    a.add('I', 'G')
    
    print("Level order:")
    a.root.for_each_level_order(vst_print)
    print("Deep first:")
    a.root.for_each_deep_first(vst_print)

    print("\nod B:")
    a.root.search('B').for_each_deep_first(vst_print)
    print("od G:")
    a.root.search('G').for_each_deep_first(vst_print)

test_drzewo()