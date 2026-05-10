size = 5
queue = [None] * size
front = -1
rear = -1


def enqueue(x):
    global front, rear

    if (rear + 1) % size == front:
        print("Overflow")
        return

    if front == -1:
        front = 0
        rear = 0
        queue[rear] = x
    else:
        rear = (rear + 1) % size
        queue[rear] = x


def dequeue():
    global front, rear

    if front == -1:
        print("Underflow")
        return

    removed = queue[front]

    if front == rear:
        front = -1
        rear = -1
    else:
        queue[front] = None
        front = (front + 1) % size

    return removed


def display():
    global front, rear

    if front == -1:
        print("Queue Empty")
        return

    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()


enqueue(1)
enqueue(2)
enqueue(3)
print("Deleted:", dequeue())
enqueue(4)
enqueue(5)
enqueue(6)

print("Queue elements:")
display()
print(queue)
print("Front:", front, "Rear:", rear)