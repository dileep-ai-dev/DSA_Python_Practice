stack1 = []
stack2 = []


def enqueue(x):
    stack1.append(x)


def dequeue():
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())

    if not stack2:
        return None

    return stack2.pop()


enqueue(10)
enqueue(20)
enqueue(30)

print("Deleted:", dequeue())
print("Deleted:", dequeue())

enqueue(40)

print("Deleted:", dequeue())