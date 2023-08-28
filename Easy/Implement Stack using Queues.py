# Implement Stack using Queues
# 2 queues
class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None: 
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        res = self.q1.pop(0)
        self.q1 = self.q2
        self.q2 = []
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

# 1 queue
class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.pop(0))

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
