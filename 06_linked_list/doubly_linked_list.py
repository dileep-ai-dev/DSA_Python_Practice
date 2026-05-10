class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def print_dll(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("NULL")


head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.prev = head

second.next = third
third.prev = second

print_dll(head)