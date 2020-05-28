"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:
"""
class MyStack:

    def __init__(self):
        from collections import deque
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return not self.q1
        
class Stack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]
    
    def empty(self):
        return not len(self._queue)
