class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next  
        self.prev = prev


class Deque:
    def __init__(self):
        self.head = None  
        self.tail = None

    def push_left(self, data):
        new_node = Node(data, next=self.head)  
        if self.head is not None:
            self.head.prev = new_node  
        else:
            self.tail = new_node  
        self.head = new_node  

    def push_right(self, data):
        new_node = Node(data, prev=self.tail) 
        if self.tail is not None:
            self.tail.next = new_node  
        else:
            self.head = new_node  
        self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("Deque is empty.")
            return None
        removed_data = self.head.data  
        self.head = self.head.next  
        if self.head is not None:
            self.head.prev = None  
        else:
            self.tail = None  
        return removed_data

    def pop_right(self):
        if self.tail is None:
            print("Deque is empty.")
            return None
        removed_data = self.tail.data  
        self.tail = self.tail.prev  
        if self.tail is not None:
            self.tail.next = None  
        else:
            self.head = None
        return removed_data

    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" <-> " if current_node.next else "\n")
            current_node = current_node.next



deque = Deque()


deque.push_left("Izquierda 1")
deque.push_right("Derecha 1")
deque.push_left("Izquierda 2")
deque.push_right("Derecha 2")


print("Estructura del Double Ended Queue:")
deque.print_structure()


print("\nPop Left:", deque.pop_left())
print("Pop Right:", deque.pop_right())


print("\nEstructura del Deque actualizada:")
deque.print_structure()
