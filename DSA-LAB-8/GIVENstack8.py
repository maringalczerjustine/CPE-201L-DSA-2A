def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("Pushed Element: " + item)

def pop(stack):
    if (is_empty(stack)):
        return "The stack is empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
push(stack, str(5))

print("The elements in the stack are:"+ str(stack))
