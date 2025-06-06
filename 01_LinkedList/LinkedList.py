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

    def append(self, value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next != None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp


# instance of linked-list
ll = LinkedList(4)
# ll.print()

ll.append(5)
ll.append(6)
ll.print()

print("calling pop")
print("poped: ", ll.pop().value)
# print("ll: ", ll.print())
