class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:       
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        else:
            return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        
        self.length += 1 
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first
        if index == self.length-1:
            return self.pop
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        temp.next = None
        temp.prev = None
        before.next = after
        after.prev = before
        
        self.length -= 1 
        return temp

    def swap_first_last(self):
        if self.length == 0:
            return False
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        return True

    def reverse(self):
        temp = self.head
        while temp is not None:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head

    def is_palindrome(self):
        if self.length <= 1:
            return True
        left = self.head
        right = self.tail
        for _ in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True
    

    def partition_list(self, x):
        if self.head is None:
            return None
        
        dummy1, dummy2 = Node(0), Node(0)
        prev1, prev2 = dummy1, dummy2
        current = self.head
        
        while current:
            if current.value < x:
                current.prev = prev1
                prev1.next = current
                prev1 = current
            else:
                current.prev = prev2
                prev2.next = current
                prev2 = current
            current = current.next
        
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        prev2.next = None
        
        self.head = dummy1.next
        self.head.prev = None

    def reverse_between(self, start_index, end_index):
        if self.length <= 0 or start_index == end_index:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        
        prev = dummy
        for i in range(start_index):
            prev = prev.next
            
        current = prev.next
        
        for i in range(end_index - start_index):
            node_to_move = current.next
            
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
            
            node_to_move.next = prev.next
            prev.next.prev = node_to_move
            prev.next = node_to_move
            node_to_move.prev = prev
            
        self.head = dummy.next
        self.head.prev = None


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)

print('\nDLL after testing append() method:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.pop()
print('\nDLL after pop() method:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.prepend(0)
print('\nDLL after prepend(0):')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(5, 10)
print('\nDLL after set_value(5, 10):')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(3, 15)
print('\nDLL after insert(3, 15):')
my_doubly_linked_list.print_list()

my_doubly_linked_list.remove(3)
print('\nDLL after remove(3):')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()
print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.reverse()
print('\nDLL after reverse():')
my_doubly_linked_list.print_list()

print('\nTesting if DLL is_palindrome():', my_doubly_linked_list.is_palindrome())

my_doubly_linked_list.partition_list()
print('\nDLL after partition list:')
my_doubly_linked_list.print_list

my_doubly_linked_list.reverse_between(2, 5)
print('\nDLL after reverse between:')
my_doubly_linked_list.print_list