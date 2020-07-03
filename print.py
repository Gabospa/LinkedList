

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def print_linked_list(self):
        node = self.head
        while node:
            print (node.data)
            node = node.next
        
    def insert_between(self, position, data):
        new_node = Node(data)
        cont = 0
        list_head = self.head
        while list_head:
            if cont == position-1:
                new_node.next = list_head.next
                list_head.next = new_node
                break
            list_head = list_head.next
            cont += 1
    


if __name__ == '__main__':
    size = int(input('Select list size: '))
    llist = LinkedList()
    for i in range(size):
        llist_item = int(input())
        llist.insert_node(llist_item)
    
    llist.print_linked_list()
    new_position = int(input('Insert new position: '))
    new_data = int(input('Insert data for New Position: '))
    llist.insert_between(new_position, new_data)
    llist.print_linked_list()


