class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        curr_node = self.head

        # remove head by setting it next node
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return 

        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def print_list(self):
        node = self.head
        while node:
            print(node.data, end=' -> ')
            node = node.next
        print("None")


llist = LinkedList()
llist.append(4)
llist.append(6)
llist.append(8)
llist.prepend(2)
llist.print_list()  # Should print: 0 -> 1 -> 2 -> 3 -> None
llist.delete_node(2)
llist.print_list()  # Should print: 0 -> 1 -> 3 -> None
