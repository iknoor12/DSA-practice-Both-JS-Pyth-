#   9 - July     Singly - Doubly linkedlist

class node2:
    def __init__(self, num):
        self.num = num
        self.next = None

class singlelist:
    def __init__(self):
        self.head = None


    #   Question  1 : Write a function to count the number of nodes in a singly linked list.
    def counting(self):
        c = 0
        current = self.head
        while current:
            c += 1
        print(c)


    #   Question  2 : Write a function to insert a new node at the end of a singly linked list.
    def insert(self, num):
        new_node = node2(num)
        curr = self.head
        while curr:
            curr = curr.next
        curr.next = new_node



class node3:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublelist:
    def __init__(self):
        self.head = None

    
    #   Question  3 : Write a function to print elements from tail to head in a doubly linked list using the prev pointer.
    def traverse(self):
        currNode = self.head
        while currNode:
            print(currNode.data, end=" <-> ")
        print("None") 


    #   Question  4 : Write a function to delete the first node that contains a specific value from the linked list.
    def delete(self):
        currentNode = self.head
        currentNode.next = self.head
