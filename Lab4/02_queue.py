# Queue implementation using a class and objects.
# A queue is FIFO (first in, first out): the first value enqueued is the
# first value dequeued.


class Queue:
    def __init__(self, size):
        self.queue = [None] * size   # fixed-size array
        self.front = 0               # index of the first element
        self.rear = -1               # index of the last element

    def is_empty(self):
        return self.front > self.rear

    def enqueue(self, value):
        if self.rear == len(self.queue) - 1:
            print("Queue overflow: cannot enqueue", value)
            return
        self.rear = self.rear + 1
        self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow: nothing to dequeue")
            return None
        dequeued = self.queue[self.front]
        self.queue[self.front] = None
        self.front = self.front + 1
        return dequeued


size = int(input("Enter the size of the queue: "))
q = Queue(size)

for i in range(size):
    value = int(input("Enter a value to enqueue: "))
    q.enqueue(value)

print("\nThe queue is:", q.queue[q.front:q.rear + 1])

dequeued = q.dequeue()
print("\nDequeued element:", dequeued)
print("The queue after dequeuing is:", q.queue[q.front:q.rear + 1])

dequeued = q.dequeue()
print("\nDequeued element:", dequeued)
