class Queue:
    def __init__(self, size):
        self.size = size
        self.list = [None] * size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

# time complexity : O(1)
    def enqueue(self, element):
        if not self.is_full():
            self.list[self.rear] = element
            self.rear = (self.rear + 1) % self.size
        else:
            print("Queue is full!")

# time complexity : O(1)
    def dequeue(self):
        if not self.is_empty():
            removed_element = self.list[self.front]
            self.front = (self.front + 1) % self.size
            return removed_element
        else:
            print("Queue is empty")
            return None

# time complexity : O(1)
    def front_element(self):
        if not self.is_empty():
            return self.list[self.front]
        else:
            print("Queue is empty")
            return None

    def print(self):
        print("Queue: ", end="")
        if self.rear >= self.front:
            for i in range(self.front, self.rear):
                print(self.list[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.list[i], end=" ")
            for i in range(0, self.rear):
                print(self.list[i], end=" ")
        print()


queue = Queue(10)

while True:
    options = '''
    1- enqueue
    2- dequeue
    3- front
    4- print
    5- exit
    '''
    command = int(input(options))

    if command == 1:
        value = int(input())
        queue.enqueue(value)
    elif command == 2:
        queue.dequeue()
    elif command == 3:
        front = queue.front_element()
        if front is not None:
            print("front element: ", front)
    elif command == 4:
        queue.print()
    elif command == 5:
        break
