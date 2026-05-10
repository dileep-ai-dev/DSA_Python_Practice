size = 5
queue = [None] * size
front = -1
rear = -1


def enqueue(x):
    global front, rear

    if rear == size - 1:
        print("Overflow")
        return

    if front == -1:
        front = 0

    rear += 1
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
        front += 1

    return removed


enqueue(10)
enqueue(20)
enqueue(30)

print("Deleted:", dequeue())
print("Queue:", queue)
print("Front:", front, "Rear:", rear)