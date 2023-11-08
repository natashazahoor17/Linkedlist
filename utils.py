#========================= Class Node =========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
#========================= Class LinkedList =========================

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    #==========================================

    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 

    #==========================================

    def add_at_index(self, data, index):
        if index < 0:
            raise ValueError("Index cannot be negative.")
        if index == 0:
            self.add_at_start(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Index out of range.")
                current = current.next
            if current is None:
                raise IndexError("Index out of range.")
            new_node.next = current.next
            current.next = new_node
 

    #==========================================
 
    def add_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
 

    #==========================================

    def update_at_index(self, data, index):
        if index < 0:
            raise ValueError("Index cannot be negative.")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("Index out of range.")
            current = current.next
        if current is None:
            raise IndexError("Index out of range.")
        current.data = data

 

    #==========================================
 
    def remove_at_start(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list.")
        self.head = self.head.next

    #==========================================

    def remove_at_end(self):
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list.")
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
 
    #==========================================

    def remove_at_index(self, index):
        if index < 0:
            raise ValueError("Index cannot be negative.")
        if self.is_empty():
            raise IndexError("Cannot remove from an empty list.")
        if index == 0:
            self.remove_at_start()
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Index out of range.")
                current = current.next
            if current is None or current.next is None:
                raise IndexError("Index out of range.")
            current.next = current.next.next

    
    #==========================================

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print("\n")
 
    #==========================================
 



    

    

    

    
    

    

    

    