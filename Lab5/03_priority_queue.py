# priority queue implementation using class and objects in python (Task 3)
# implemented as a min-heap : the smallest priority is removed first


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # move an element up until the heap property is restored
    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self._swap(index, parent)
                index = parent
            else:
                break

    # move an element down until the heap property is restored
    def _sift_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break
            self._swap(index, smallest)
            index = smallest

    # insert a value into the priority queue
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    # look at the smallest value without removing it
    def peek(self):
        return self.heap[0]

    # remove and return the smallest value
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        smallest = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return smallest


size = int(input("Enter the number of elements : "))
pq = PriorityQueue()

for i in range(size):
    value = int(input("Enter the value : "))
    pq.insert(value)

print("\nThe priority queue (heap) is :", pq.heap)
print("The smallest element is :", pq.peek())

print("\nRemoving the elements in priority order :")
while not pq.is_empty():
    print(" ", pq.extract_min())
