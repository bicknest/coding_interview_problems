class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) is 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) is 0:
            return None
        return self.items[-1]


class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if self.max_stack.peek() is None or self.max_stack.peek() < item:
            self.max_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item is self.max_stack.peek():
            self.max_stack.pop()

        return item

    def get_max(self):
        return self.max_stack.peek()
