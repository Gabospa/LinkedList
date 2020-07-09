
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        self.head = new_node


    def insert_node(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            node.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

    def print_list_forward(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
    
    def print_list_backward(self):
        node = self.tail
        while node:
            print (node.data)
            node = node.prev
        
    def insert_between(self, position, data):
        new_node = Node(data)
        cont = 0
        list_head = self.head
        while list_head:
            if cont == position-1:
                if list_head.prev == None:
                    self.head = new_node
                
                new_node.next = list_head.next
                new_node.prev = list_head
                list_head.next = new_node
                temp = new_node
                new_node = new_node.next
                new_node.prev = temp
                break
            list_head = list_head.next
            cont += 1

    

    def delete_node(self, position):
        cont = 0
        node = self.head
        
        if node is not None:
            if position == -1:
                self.head = node.next
                node = None

        while node:
            if cont == position -1:
                prev = node
                node = node.next
                prev.next = node.next
                node = None
                break
            cont += 1



if __name__ == '__main__':
    size = int(input('Select list size: '))
    llist = DLinkedList()
    for i in range(size):
        llist_item = int(input())
        llist.insert_node(llist_item)
    
    llist.print_list_forward()
    print('\n')
    new_position = int(input('Insert new position: '))
    new_data = int(input('Insert data for New Position: '))
    llist.insert_between(new_position, new_data)
    # llist.print_list_forward()
    # print('\n')
    # new_start = int(input('Insert new start data: '))
    # llist.insert_at_start(new_start)
    # llist.print_list_forward()
    # llist.delete_node(int(input('Delete position: ')))
    # llist.print_list_forward()
    llist.print_list_backward()
    print('\n')
    llist.print_list_forward()

