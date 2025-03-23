class Node:
    def __init__(self,key):
        self.prev = None
        self.value = key
        self.next = None

class DoubleLinkedList:
    def __init__(self,key):
        self.head = Node(key)

    def println(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def append(self,key):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        new_node = Node(key)
        current_node.next = new_node
        new_node.prev = current_node

    def delete(self,key):
        prev_node = None
        next_node = None
        if self.head.value == key:
            self.head = self.head.next
            self.head.prev = None
            return
        current_node = self.head
        found = 0
        while current_node is not None:
            if current_node.value == key: # 2 == 2
                prev_node = current_node.prev # 5
                next_node = current_node.next # 6
                found = 1
                break
            current_node = current_node.next
        if found != 1:
            return
        current_node = next_node # 2 = 6
        prev_node.next = current_node # 2 = 6
        current_node.prev = prev_node # 2 = 5

    def reverse(self,key):
        current_node = self.head
        found = 0
        while current_node.value is not None:
            if current_node.value == key:
                found = 1
                break
            current_node = current_node.next
        if found != 1:
            print("not found")
            return
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.prev



if __name__ == "__main__":
    d = DoubleLinkedList(4)
    d.append(9)
    d.append(5)
    d.append(2)
    d.append(6)
    d.append(3)
    d.println()
    print("=============delete-header==============")
    d.delete(4)
    d.println()
    print("=============delete-any=================")
    d.delete(2)
    d.println()
    print("=============reverse====================")
    d.reverse(3)