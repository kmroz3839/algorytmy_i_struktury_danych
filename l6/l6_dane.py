from typing import Any, List
import graphviz

class BinaryNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.left_child: 'BinaryNode' = None
        self.right_child: 'BinaryNode' = None
    
    def min(self) -> 'BinaryNode':
        if self.left_child is not None:
            return self.left_child.min()
        else:
            return self
    
    def contains(self, value: Any, vret: List[bool]):
        if vret[0]:
            return
        if self.value == value:
            vret[0] = True
        elif value > self.value and self.right_child is not None:
            self.right_child.contains(value, vret)
        elif self.left_child is not None:
            self.left_child.contains(value, vret)

    def assign_child(self, which: int, target: 'BinaryNode'):
        if which == 0:
            self.left_child = target
        else:
            self.right_child = target
    
    def prt(self, layer:int = 0):
        r = ""
        for x in range(layer):
            r += "-"
            r += ">"
        print(r+str(self.value))
        for x in [self.left_child, self.right_child]:
            if x is not None:
                x.prt(layer + 1)
    
    def generate_graphviz_edges(self, g: graphviz.Graph) -> None:
        if self.left_child is not None:
            g.edge(str(self.value), str(self.left_child.value))
            self.left_child.generate_graphviz_edges(g)
        if self.right_child is not None:
            g.edge(str(self.value), str(self.right_child.value))
            self.right_child.generate_graphviz_edges(g)


class BinarySearchTree:
    def __init__(self, value: Any):
        self.root: 'BinaryNode' = BinaryNode(value)

    def _insert(self, entry: BinaryNode, value: Any) -> BinaryNode:
        if entry.value > value:
            if entry.left_child is not None:
                self._insert(entry.left_child, value)
            else:
                print("assigning l")
                entry.left_child = BinaryNode(value)
        else:
            if entry.right_child is not None:
                self._insert(entry.right_child, value)
            else:
                print("assigning r")
                entry.right_child = BinaryNode(value)
        return BinaryNode(value)
    
    def insert(self, value: Any) -> None:
        self._insert(self.root, value)
    
    def insert_list(self, list_: List[Any]):
        for x in list_:
            self.insert(x)
    
    def contains(self, value: Any) -> bool:
        vret: List[bool] = [False]
        self.root.contains(value, vret)
        return vret[0]
    
    def remove(self, value: Any) -> None:
        ttarget = BinaryNode(None)
        ttarget.right_child = self.root
        self._remove(ttarget, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
       
        ops = [node.left_child, node.right_child]
        for x in range(0,2):
            op_target: BinaryNode = ops[x]
            if op_target is not None:
                if op_target.value == value:
                    # brak dzieci
                    if op_target.left_child is None and op_target.right_child is None:
                        node.assign_child(x, None)
                    # jedno dziecko
                    elif (op_target.left_child is None) != (op_target.right_child is None):
                        if op_target.left_child is not None:
                            node.assign_child(x, op_target.left_child)
                        else:
                            node.assign_child(x, op_target.right_child)
                    # oba
                    else:
                        val: Any = op_target.right_child.min().value
                        self.remove(val)
                        op_target.value = val
                else:
                    if node.value is None or (x == 0 and value < node.value) or (x == 1 and value > node.value):
                        self._remove(op_target, value)
    
    def show(self):
        g = graphviz.Graph('BinaryTree')
        self.root.generate_graphviz_edges(g)
        g.render('BinaryTree', view = True)

if __name__ == "__main__":
    ntree = BinarySearchTree(8)
    ntree.insert_list([3, 10, 1, 6, 14, 4, 7, 13])
    ntree.root.prt()
    ntree.remove(14)
    print("-----")
    ntree.root.prt()
    ntree.show()