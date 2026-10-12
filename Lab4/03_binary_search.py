# Binary search implemented using a class and objects.
# The array is sorted first (bubble sort), because binary search only
# works on ordered data.


class BinarySearch:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = (
                        self.array[j + 1], self.array[j]
                    )

    def search(self, target):
        low = 0
        high = len(self.array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


array = [23, 56, 70, 88, 90, 99, 12, 34, 9, 5]
bs = BinarySearch(array)
bs.bubble_sort()
print("Sorted array:", array)

target = int(input("Enter the number to search: "))
result = bs.search(target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
