class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_element_start(self, data):
        node = Node(data)
        tmp = self.head
        node.next = tmp
        self.head = node
        self.count += 1

    def insert_element_end(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            node = self.head
            while node:
                if node.next is None:
                    node.next = Node(data)
                    break
                else:
                    node = node.next
        self.count += 1

    def get_length(self):
        return self.count

    def remove_at(self, index):
        if self.head is None:
            print("Linked List is empty")
            return

        if 0 > index > self.count:
            raise Exception("not valid index")

        if index == 0:
            self.head = self.head.next

        count = 0
        node = self.head

        while node:
            if count == index - 1:
                node.next = node.next.next
                break
            else:
                node = node.next
                count += 1

    def insert_at(self, index, data):
        if index == 0:
            node = Node(data)
            tmp = self.head
            self.head = node
            self.head.next = tmp
            self.count += 1

        counter = 0
        node = self.head
        while node:
            if counter == index -1:
                new_node = Node(data)
                tmp = node.next
                node.next = new_node
                new_node.next = tmp
                break
            else:
                node = node.next
                counter += 1

    def insert_value_after(self, val, data):
        node = self.head

        while node:
            if node.data == val:
                new_node = Node(data)
                tmp = node.next
                node.next = new_node
                new_node.next = tmp
                break
            else:
                node = node.next

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return

        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next


l1 = LinkedList()

l1.insert_element_end(1)
l1.insert_element_end(2)
l1.insert_element_end(3)
l1.print_list()
print()
l1.insert_at(2, 6)
l1.print_list()
print()
l1.insert_value_after(2, 8)
l1.print_list()
print()
print(l1.get_length())
