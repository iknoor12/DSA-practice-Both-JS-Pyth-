#   Define  a  class
class node:
    def __init__(self, name):
        self.name = name
        self.next = None

class linkedlist:
    def __init__(self, name):
        self.head = None             #   head  initialzation


    #   Insertion  at  beginning
    def insert_at_beginning(self, name):
        new_node = node(name)        #   Create  nodes ->  node_name = class_name(value)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} is inserted at beginning successfully!")



    #   Insertion  at  end 
    def insert_at_end(self, name):
        new_node = node(name)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{name} is inserted at end successfully!")



    #   Deletion  
    def delete(self, key):
        current = self.head
        prev = None
        while current and current.name == key:
            prev.next = current.next
            print(f"{key} is deleted successfully!")

            if self.head is None:
                print("Your list is empty. Can't delete!")

    

    #   Display  list
    def display(self):
        curr = self.head
        while curr:
            print(curr.name, end=" -> ")
            curr = curr.next
        print("None")



    #   Search  an  element  in  list
    def search(self, name):
        curr = self.head
        if self.head is None:
            print("Your list is empty!")
        else:
            position = 0
            while curr:
                if curr.name == name:
                    print(f"{name} is found at {position}.")
                    return
                curr = curr.next
                position += 1
            else:
                print(f"Couldn't found {name}.")


if __name__ == "__main__":
    ll = linkedlist('name')
    print("/nMenu:")
    print("1. Insert Student Name in the beginning")
    print("2. Insert Student Name")
    print("3. Search Student Name")
    print("4. Display All Student Name")
    print("5. Delete Student Name")
    print("6. Exit")

    while True:

        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            name = input("Enter a name to insert at beginning: ")
            ll.insert_at_beginning(name)

        elif choice == "2":
            name = input("Enter a name to insert at end: ")
            ll.insert_at_end(name)

        elif choice == "3":
            print("Enter a name to search: ")
            ll.search(name)

        elif choice == "4":
            ll.display()

        elif choice == "5":
            name = input("Enter the name to delete: ")
            ll.delete(name)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

