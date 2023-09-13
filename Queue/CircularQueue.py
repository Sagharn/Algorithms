class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, element):
        if not self.is_full():
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            print("Queue is full!")

    def dequeue(self):
        if not self.is_empty():
            removed_element = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return removed_element
        else:
            print("Queue is empty!")
            return None

    def front_element(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            print("Queue is empty!")
            return None

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return (self.size - self.front) + (self.rear + 1)

    def print(self):
        if not self.is_empty():
            current = self.front
            while True:
                print(self.queue[current], end=" ")
                if current == self.rear:
                    break
                current = (current + 1) % self.size
            print()
        else:
            print("Queue is empty!")


circular_queue = CircularQueue(5)

circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)

circular_queue.print()

print("Deleted element:", circular_queue.dequeue())
print("Deleted element:", circular_queue.dequeue())

circular_queue.print()
