
class node4:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlecircularlist:
    def __init__(self):
        self.head = None


    def insert_At_Beginning(self, data):
        new_node = node4(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head

        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head
            self.head = new_node
            


    def insert_at_end(self, data):
        new_node = node4(data)
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head


    # def display(self):
        