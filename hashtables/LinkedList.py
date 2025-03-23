class Node:
    def __init__(self,key):
        self.value = key
        self.next = None

class LinkedList:
    def __init__(self,key):
        self.head = Node(key)

    def print_linked_list(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next

    def append(self,key):
        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = Node(key)

    def prepend(self,key):
        pointer = Node(key)
        pointer.next = self.head
        self.head = pointer

    def insert(self,position,key):
        length = 0
        pointer = self.head
        if length == position:
            newNode = Node(key)
            newNode.next = pointer
            self.head = newNode
            return
        while pointer.next is not None:
            length+=1
            if length == position:
                remaining = pointer.next
                new_node = Node(key)
                pointer.next = new_node
                new_node.next = remaining
                return
            pointer = pointer.next
    def delete(self,value):
        prev = None
        if self.head.value == value:
            self.head = self.head.next
            return
        pointer = self.head
        while pointer is not None:
            if pointer.value == value:
                break
            prev = pointer
            pointer = pointer.next
        prev.next = pointer.next

    def reverse(self,key):
        rev = []
        pointer = self.head
        found = 0
        while pointer.value is not None:
            rev.append(pointer.value)
            if pointer.value == key:
                found = 1
                break
            pointer = pointer.next
        if found != 1:
            print("not reversible as value is not present")
            return
        rev.reverse()
        print(rev)

if __name__ == "__main__":
    l = LinkedList(5)
    l.append(6)
    l.append(7)
    l.prepend(1)
    l.append(8)
    l.print_linked_list()
    print("==========insertion example====================")
    l.insert(2,9)
    l.print_linked_list()
    print("======deletion example=========")
    l.delete(6)
    l.print_linked_list()
    print("========reverse==============")
    l.reverse(8)