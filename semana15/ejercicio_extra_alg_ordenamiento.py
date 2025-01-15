class Node:
    data: int
    next: "Node"


    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node


    def __init__(self, head):
        self.head = head


    def sort_structure(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            current = self.head
            swapped = False
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data #Aca aplique algo que se llama desempaquetado multiple
                    swapped = True
                current = current.next


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


third_node = Node(45)
second_node = Node(75, third_node)
first_node = Node(1, second_node)


linked_list = LinkedList(first_node)
print("Unsorted list:")
linked_list.print_list()

linked_list.sort_structure()
print("Sorted list:")
linked_list.print_list()