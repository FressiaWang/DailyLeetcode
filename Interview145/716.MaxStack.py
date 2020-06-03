"""
Design a max stack that supports push, pop, top, peekMax and popMax.
push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. 
If you find more than one maximum elements, only remove the top-most one.
"""
class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.max_stack = []
    def push(self, x):
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))
     def pop(self):
         self.max_stack.pop()
         return self.stack.pop()
     def top(self):
         return self.stack[-1] if self.stack else None
     def peekMax(self):
         return self.max_stack[-1] if self.max_stack else None
     def popMax(self):
         val = self.peekMax()
         temp = []
         while self.top() != val:
             temp.append(self.pop())
         self.pop()
         while temp:
             self.push(temp.pop())
         return val
