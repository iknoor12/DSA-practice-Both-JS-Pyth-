#   Double  linkedlist

#   Define  a  class
class node1:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None             #   head  initialzation


    #   Insertion  at  beginning
    def insert_at_beginning(self, num):
        new_node = node1(num)
        if self.head is None:
            self.head = new_node
            print(f"${num} is added at beginning.")
        else:
            new_node.next = self.head
            self.head.prev = new_node



    #   Insertion  at  end
    def insert_at_end(self, num):
        new_node = node1(num)
        current = self.head
        if self.head is None:
            self.head = new_node
            print(f"Your list was enpty, So, ${num} is inserted at beginning successfully!")

        while current:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"Given ${num} is added at end successfully!")



    #   Deletion  
    def delete(self, key):
        if self.head == key:                       #  when we want to delete head
            self.head = self.head.next
            print(f"${key} is deleted successfully!")

        else:
            curr = self.head
            while curr and curr.data == key:       #  any element inside the list
                curr.prev.next = curr.next
                print(f"${key} is deleted successfully!")
            else:
                print("Can't delete")




    #   Display 
    def display(self, num):
        current = self.head
        while current:
            print("You list: ", num, end=" <-> ")
            current = current.next
        print("None")



    #   Search  an  element  in  list
    def search(self, ele):
        position = 0
        curr = self.head
        while curr:
            if curr.data == ele:
                print(f"${ele} found at ${position}.")
                return
            curr = curr.next
            position += 1
        else:
            print(f"Doesn't found ${ele}.")

