class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def countNodes(self):
        node = self.head
        count = 1
        while node.next is not None:
            count += 1
            node = node.next
        return count

    def printAllElm(self):
        n = self.head
        print(n.val)
        while n.next is not None:
            n = n.next
            print(n.val)

    def insertAtBegin(self, Node):
        Node.next = self.head
        self.head = Node

    def insertAtTheEnd(self, Node):
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = Node

    def removeElement(self, key):
        no = self.head
        while no.next is not None:
            if no.val == key:
                break
            prev = no
            no = no.next

        next = no.next
        prev.next = next
        no = None



head = Node(1)
n0 = Node(2)
n1 = Node(3)
n2 = Node(4)
n3 = Node(5)
n4 = Node(1111)
n5 = Node(222222)

myLinkedList = LinkedList()
myLinkedList.head = head
head.next = n0
n0.next = n1
n1.next = n2
n2.next = n3

# print(myLinkedList.countNodes())

myLinkedList.insertAtBegin(n4)
myLinkedList.insertAtTheEnd(n5)

myLinkedList.removeElement(222222)

myLinkedList.printAllElm()

queue = []

queue.insert(0, "2")
queue.insert(0, "3")

print(queue)
