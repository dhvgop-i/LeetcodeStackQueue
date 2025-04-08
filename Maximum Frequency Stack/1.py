from collections import defaultdict
from queue import LifoQueue

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(LifoQueue)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f

        if f > self.maxfreq:
            self.maxfreq = f

        self.group[f].put(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].get()

        self.freq[val] -= 1

        if self.group[self.maxfreq].empty():
            self.maxfreq -= 1

        return val
