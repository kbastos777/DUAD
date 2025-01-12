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

    def print_sorted_structure(self):
            current_node = self.head
            number_list=[]
            while (current_node is not None):
                    number_list.append(current_node.data)
                    current_node = current_node.next
            for out_index in range(0,len(number_list)-1,):
                has_made_changes = False
                print(number_list)
                for inside_index in range(0,len(number_list)-1,):
                    current_index = number_list[inside_index]
                    next_index = number_list[inside_index + 1]
                    if current_index < next_index:
                        number_list[inside_index]=next_index
                        number_list[inside_index+1]=current_index
                        has_made_changes = True
                    out_index = out_index + 1    
                if not has_made_changes:
                    return

third_node = Node(45)
second_node = Node(75, third_node)
first_node = Node(1, second_node)

linked_list = LinkedList(first_node)
linked_list.print_sorted_structure()