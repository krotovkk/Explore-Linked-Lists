from random import randint

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linked_list:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
        print('\n')

    def insert(self,head,data):
    #Complete this method
        if head is None:
            head = node(data)
        elif head.next is None:
            head.next = node(data)
        else:
            self.insert(head.next, data)
        return head
    
    def remove(self, head, data):
        if head is None:
            return
        if head.data == data:
            head = head.next
        elif head.next.data == data:
            head.next = head.next.next
        else:
            self.remove(head.next, data)
        return head




mylist= linked_list()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    

mylist.display(head); 