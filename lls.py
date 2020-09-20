#each node has :
# value : integer
# next pointer : points to the next node
class node:
    def __init__(self,value=0):
        self.value=value
        self.next=None

#each lined list has :
# a head pointer pointing to the first node of the linked list.
class linked_list:
    def __init__(self):
        self.head=node()
    
    def count(self):
        pointer = self.head #creating a pointer pointing to the head of the list
        length = 1
        while(pointer.next != None):    #traversing the list and counting the elements simultaneously
            length +=1
            pointer = pointer.next
        return length

    def insert_at_end(self,quantity):
        pointer = self.head # create a pointer to the head of the list
        new_node = node(quantity)   # arranging a new node of the desired value
        while(pointer.next != None):
            pointer = pointer.next  #traversing to the end of the list
        pointer.next = new_node #making the last element point to the new node
        return 

    def show_list(self):
        ptr = self.head # create a pointer to the head of the list
        for i in range(self.count()):
            print("->",ptr.value,end=" ")   #traversing the list and displaying the value of each node simultaneously
            ptr = ptr.next
        return 

    def show_element(self,position):
        #displays element at "position"
        #indexing starts from 1
        if(position>self.count()):
            return False
        else:
            current_position=1
            ptr=self.head
            while(current_position!=position):
                ptr = ptr.next
                current_position+=1
            return ptr.value
        
ll= linked_list()
ll.insert_at_end(3)
ll.insert_at_end(1)
ll.insert_at_end(5)
ll.insert_at_end(7)
ll.show_list()
print("\nNumber of elements in the list are:",ll.count())
print("The element at",9,"position is:",ll.show_element(9))