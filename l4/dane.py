from typing import Any


class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next

class LinkedList:

    def push(self, value: Any) -> None:
        nnode: Node = Node(value, self.head)
        self.head = nnode
        if self.tail == None:
            self.tail = nnode

    def append(self, value: Any) -> None:
        nnode: Node = Node(value, None)
        if self.tail != None:
            self.tail.next = nnode
        self.tail = nnode
        if self.head == None:
            self.head = nnode

    def node(self, at: int) -> Node:
        cnode: Node = self.head
        for x in range(0, at):
            if cnode != None:
                cnode = cnode.next
            else:
                raise IndexError(f"index {at} poza zasięgiem listy")
        return cnode

    def insert(self, value: Any, after: Node) -> Node:
        cnode = self.head
        while cnode != None:
            if cnode == after:
                nnode = Node(value, cnode.next)
                cnode.next = nnode
                return nnode
            cnode = cnode.next
        raise ValueError("nie znaleziono")

    def pop(self):
        rnode = self.head
        if rnode != None:
            self.head = self.head.next
        if self.head == None:
            self.head = self.tail = None
        return rnode.value
    
    def remove_last(self) -> Any:
        if len(self) >= 2:
            el = len(self)-2
            ret: Any = self.node(el).next.value
            self.node(el).next = None
            return ret
        elif len(self) == 1:
            ret: Any = self.head.value
            self.head = self.tail = None
            return ret
        else:
            return None

    def remove(self, after: Node) -> Any:
        cnode = self.head
        while cnode != None:
            if cnode == after:
                if cnode.next != None:
                    rval: Any = cnode.next.value
                    cnode.next = cnode.next.next
                    return rval
                return None
            cnode = cnode.next
        raise ValueError("nie znaleziono")

    def __len__(self):
        i = 0
        cnode = self.head
        while cnode != None:
            cnode = cnode.next
            i += 1
        return i
    
    def __str__(self):
        ret: str = ""
        cnode = self.head
        while cnode != None:
            ret += str(cnode.value) 
            if cnode.next != None:
                ret += " -> "
            cnode = cnode.next
        return ret

#zadanie 2
class Stack:

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)
    
    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self):
        cnode = self._storage.head
        while cnode != None:
            print(cnode.value)
            cnode = cnode.next
    
    def __len__(self):
        return len(self._storage)

#zadanie 3
class Queue:

    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.node(0).value
    
    def enqueue(self, element: Any) -> None:
        self._storage.append(element)
    
    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self):
        r = ""
        for x in range(0, len(self._storage)):
            r += self._storage.node(x).value
            if x != len(self._storage)-1:
                r += ", "
        return r
    
    def __len__(self):
        return len(self._storage)
