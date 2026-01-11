
# Contact class to store contact details
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Node:
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_contact(self, contact):
        new_node = Node(contact)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        if not current:
            print("No contacts found.")
            return
        while current:
            print(f"{current.contact.name} - {current.contact.phone}")
            current = current.next

    def display_backward(self):
        current = self.tail
        if not current:
            print("No contacts found.")
            return
        while current:
            print(f"{current.contact.name} - {current.contact.phone}")
            current = current.prev


def substring_search(text, pattern):
    """ Naive substring search """
    text = text.lower()
    pattern = pattern.lower()

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return True
    return False



# Main Program

contacts_list = DoublyLinkedList()
contacts_dict = {}  # Hash table {name: Contact}

while True:
    print("\n1. Add Contact")
    print("2. Search by Keyword")
    print("3. Search by Exact Name")
    print("4. View All (Forward)")
    print("5. View All (Backward)")
    print("6. Exit")

    choice = input("\nEnter option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")

        if name in contacts_dict:
            print("Contact already exists.")
        else:
            contact = Contact(name, phone)
            contacts_list.add_contact(contact)
            contacts_dict[name] = contact
            print("Contact added.")

    elif choice == "2":
        keyword = input("Search keyword: ")
        found = False

        for contact in contacts_dict.values():
            if substring_search(contact.name, keyword):
                print(f"Match found: {contact.name} - {contact.phone}")
                found = True

        if not found:
            print("No matching contacts found.")

    elif choice == "3":
        name = input("Enter exact name: ")
        if name in contacts_dict:
            contact = contacts_dict[name]
            print(f"Contact found: {contact.name} - {contact.phone}")
        else:
            print("Contact not found.")

    elif choice == "4":
        print("\nContacts (Forward):")
        contacts_list.display_forward()

    elif choice == "5":
        print("\nContacts (Backward):")
        contacts_list.display_backward()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
