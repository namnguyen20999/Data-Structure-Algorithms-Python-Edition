class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


# Head is the first node in the list of nodes

# Tail is the last node in the list of nodes


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_array(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.tail
        
        while temp.next is not None:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp
    
    def preappend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if temp.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
        self.length -= 1
        return temp
    
    def get(self, index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,value, index):
        temp = self.get(index)
        if(temp):
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.preappend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        # This is O(n) of getting temp
        # Becasue we need to use get fucntion
        # Which means we need to loop through the list of nodes
        
        # pre = self.get(index - 1)
        # temp = self.get(index)
        
        # This is O(1)
        # Because we do not need to loop through the list of nodes
        # We user pre.next which ultilize the atribute "next" in our Node
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        return temp
    
arr = LinkedList(1)
arr.append(3)
arr.preappend(5)
arr.set_value(10,0)
arr.insert(2, 7)
arr.remove(2)
arr.print_array()