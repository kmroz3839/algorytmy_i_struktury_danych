from typing import Any, Callable, List, Union, Tuple
from dane import Queue, Stack
from treeviz.treeviz import Node
import networkx as nx
import matplotlib.pyplot as plt
import graphviz

class TreeNode:

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
    
    def for_each_deep_first_reverse(self, visit: Callable[['TreeNode'], None]) -> None:
        for x in self.children:
            x.for_each_deep_first_reverse(visit)
        visit(self)
        
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        nq = Queue()
        for x in self.children:
            nq.enqueue(x)
        while len(nq) > 0:
            nqe: TreeNode = nq.dequeue()
            visit(nqe)
            a = nqe.children
            for y in a:
                nq.enqueue(y)
    
    def for_each_level_order_right(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        nq = Queue()
        for x in self.children[::-1]:
            nq.enqueue(x)
        while len(nq) > 0:
            nqe: TreeNode = nq.dequeue()
            visit(nqe)
            for y in nqe.children[::-1]:
                nq.enqueue(y)

    def for_each_level_order_reverse(self, visit: Callable[['TreeNode'], None]) -> None:
        nq = Queue()
        visitQ = Stack()
        for x in self.children:
            nq.enqueue(x)
        while len(nq) > 0:
            nqe: TreeNode = nq.dequeue()
            for y in nqe.children:
                nq.enqueue(y)
            visitQ.push(nqe)
        while len(visitQ) > 0:
            visit(visitQ.pop())
        visit(self)
    
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
    
    def to_treeviz_node(self) -> Node:
        rt = Node(self.value)
        for x in self.children:
            rt.add_child(x.to_treeviz_node())
        return rt

    def generate_graphviz_edges(self, g: graphviz.Graph) -> None:
        for x in self.children:
            g.edge(str(self.value), str(x.value))
            x.generate_graphviz_edges(g)

    def generate_nxtree_branches(self, g: List) -> None:
        for x in self.children:
            g.append([str(self.value), str(x.value)])
            x.generate_nxtree_branches(g)

    def __str__(self):
        return str(self.value)

class Tree:
    #root: TreeNode

    def __init__(self, v: Any):
        if isinstance(v, TreeNode):
            self.root = v
        else:
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
    
    def for_each_level_order_reverse(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order_reverse(visit)
    
    def for_each_deep_visit_reverse(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first_reverse(visit)
    
    def to_treeviz_tree(self) -> Node:
        return self.root.to_treeviz_node()

    def generate_nx_tree(self) -> nx.Graph:
        #ret = graphviz.Graph('Tree', engine='sfdp')
        ret = nx.Graph()
        a: List[Tuple[str,str]] = []
        self.root.generate_nxtree_branches(a)
        ret.add_edges_from(a)
        return ret

    def generate_graphviz_tree(self) -> graphviz.Graph:
        ret = graphviz.Graph('Tree')
        self.root.generate_graphviz_edges(ret)
        return ret

    def show(self):
        #nx.draw_networkx(self.generate_graphviz_tree())
        #plt.show()

        #self.to_treeviz_tree().visualize()

        self.generate_graphviz_tree().render('Tree', view = True) 


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
    a.add('H', 'I')
    
    print("Deep first:")
    #print("Normalnie:")
    a.root.for_each_deep_first(vst_print)
    #print("reverse:")
    #a.root.for_each_deep_first_reverse(vst_print)

    print("Level order:")
    a.root.for_each_level_order(vst_print)
    #print("reverse:")
    #a.root.for_each_level_order_reverse(vst_print)

    print("\nod B:")
    a.root.search('B').for_each_deep_first(vst_print)
    print("od G:")
    a.root.search('G').for_each_deep_first(vst_print)

    a.show()

def test_drzewo2():
    treenode = TreeNode(6)
    treenode.add(TreeNode(2))
    treenode.add(TreeNode(7))
    treenode.children[0].add(TreeNode(1))
    treenode.children[0].add(TreeNode(4))

    tree = Tree(treenode)
    tree.add(3, tree.root.children[1].value)
    tree.add(5, tree.root.children[0].value)
    tree.add(9, tree.root.search(7).value)
    tree.add(8, tree.root.search(9).value)

    tree.root.for_each_level_order(vst_print)
    print("od lewej")
    tree.root.for_each_level_order_right(vst_print)

    tree.show()

#test_drzewo()
test_drzewo2()
