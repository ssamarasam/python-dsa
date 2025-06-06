# Singly Linked List
# each node has a value and next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def print(self):
        temp = self.head
        while (temp != None):
            print(temp.value)
            temp = temp.next


# instance of linked-list

ll = LinkedList(4)
ll.print()
