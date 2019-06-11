from random import randint


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
        print('\n')

    def insert(self, head, data):
        if head is None:
            head = Node(data)
        elif head.next is None:
            head.next = Node(data)
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


if __name__ == '__main__':
    mylist = LinkedList()
    T = 15
    head = None
    for i in range(T):
        data = randint(1, 100)
        head = mylist.insert(head, data)

    mylist.display(head)