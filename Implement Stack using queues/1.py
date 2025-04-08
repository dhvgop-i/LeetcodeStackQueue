from queue import Queue

class MyStack:
    def __init__(self):
        self.data = Queue()

    def push(self, x: int) -> None:
        self.data.put(x)
        
    def pop(self) -> int:
        right = Queue()
        res = None
        while not self.data.empty():
            if res:
                right.put(res)
            res = self.data.get()
        
        while not right.empty():
            self.data.put(right.get())

        return res

    def top(self) -> int:
        right = Queue()
        res = None
        while not self.data.empty():
            if res:
                right.put(res)
            res = self.data.get()
        
        while not right.empty():
            self.data.put(right.get())
        self.data.put(res)
        return res

    def empty(self) -> bool:
        return self.data.empty()
