from queue import LifoQueue

class MyQueue:
    def __init__(self):
        self.left = LifoQueue()
        self.right = LifoQueue()
        self.__size = 0

    def push(self, x: int) -> None:
        self.left.put(x)
        self.__size += 1

    def pop(self) -> int:
        res = None
        while not self.left.empty():
            self.right.put(self.left.get())
        res = self.right.get()

        while not self.right.empty():
            self.left.put(self.right.get())
        
        self.__size -= 1
        
        return res

    def peek(self) -> int:
        res = None
        while not self.left.empty():
            self.right.put(self.left.get())
        res = self.right.get()
        self.right.put(res)

        while not self.right.empty():
            self.left.put(self.right.get())
        
        return res

    def empty(self) -> bool:
        return self.left.empty()
