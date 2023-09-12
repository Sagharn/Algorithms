# time complexity : O(1)
class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            if popped_item == self.min_stack[-1]:
                self.min_stack.pop()
            return popped_item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def get_min(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        else:
            return None


my_stack = StackWithMin()
my_stack.push(5)
my_stack.push(3)
my_stack.push(8)
my_stack.push(2)

print(my_stack.get_min())
