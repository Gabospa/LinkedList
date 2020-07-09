class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLinkedList:
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
        node.next = self.head


    def print_linked_list(self):
        node = self.head
        while node.next is not self.head:
            print (node.data)
            node = node.next


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
    llist = CLinkedList()
    for i in range(size):
        llist_item = int(input())
        llist.insert_node(llist_item)
    
    llist.delete_node(int(input('Delete position: ')))
    llist.print_linked_list()
    