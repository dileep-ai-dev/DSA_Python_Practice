class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    return head


def delete_pos(head, pos):
    if head is None:
        return None

    if pos == 1:
        return head.next

    temp = head
    count = 1

    while temp.next and count < pos - 1:
        temp = temp.next
        count += 1

    if temp.next is None:
        return head

    temp.next = temp.next.next
    return head


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("NULL")


head = Node(10)
head = insert_end(head, 20)
head = insert_end(head, 30)
head = insert_end(head, 40)

print("Before delete:")
print_list(head)

head = delete_pos(head, 2)

print("After delete:")
print_list(head)