class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity  # fixed-size storage

    def get(self, i: int) -> int:
        # assume i is valid
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # assume i is valid
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # assume non-empty
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None  # optional: clear reference
        self.size -= 1
        return val

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
