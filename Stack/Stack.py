class Stack:
    def __init__(self, size):
        self.size = size
        self.list = [None] * size
        self.index = 0
        
# time complexity : O(1)
    def push(self, element):
        if self.index == self.size:
            return 0
        self.list[self.index] = element
        self.index += 1
        
# time complexity : O(1)
    def pop(self):
        if self.index == 0:
            return 0
        self.index -= 1
        
# time complexity : O(1)
    def top(self):
        return self.list[self.index - 1]

    def get_size(self):
        return self.index
        
# time complexity : O(n)
    def min(self):
        minimum = self.list[0]
        for i in range(1, self.index):
            if self.list[i] < minimum:
                minimum = self.list[i]
        return minimum


    def print(self):
        print("Stack: ")
        for i in range(self.index):
            print(self.list[i], end=" ")


stack = Stack(20)
while True:
    options = '''
    1- push
    2 - pop 
    3- top 
    4- size
    5 - min 
    6 - sort
    7 - print stack
    8 - exit
    '''
    command = int(input(options))
    if command == 1:
        value = int(input())
        stack.push(value)
    elif command == 2:
        stack.pop()
    elif command == 3:
        print(stack.top())
    elif command == 4:
        print(stack.get_size())
    elif command == 5:
        print(stack.min())
    elif command == 6:
        stack.sort()
    elif command == 7:
        stack.print()
    elif command == 8:
        break
