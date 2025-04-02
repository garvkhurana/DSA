"""class linkedlist:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        print(data)
        print(next)
        
        
    """
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class ll:
    def __init__(self):
        self.head=None

    def append_elements(self,data):
         new_node = node(data)
         if not self.head:
            self.head = new_node
            return
         pointer = self.head
         while pointer.next:
            pointer = pointer.next
         pointer.next = new_node
        
        
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("end of the list")    
            
            

linked_list=ll()
linked_list.append_elements(10)  
linked_list.append_elements(20) 
linked_list.append_elements(30) 
linked_list.append_elements(40)   
linked_list.display()        
            
        
                      