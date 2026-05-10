class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original:")
print_list(head)

head = reverse_list(head)

print("Reversed:")
print_list(head)