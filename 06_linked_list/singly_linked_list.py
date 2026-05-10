class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


# Creating Linked List
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

print_list(head)