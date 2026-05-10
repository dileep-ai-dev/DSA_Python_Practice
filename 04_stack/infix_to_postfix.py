def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(s):
    stack = []
    output = ""

    for ch in s:
        if ch.isalnum():
            output += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:
            while stack and priority(stack[-1]) >= priority(ch):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


print(infix_to_postfix("A+B*C-D"))