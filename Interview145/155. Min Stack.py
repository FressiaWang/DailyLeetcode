"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x: 'int') -> 'None':
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self) -> 'None':
        if len(self.data) > 1: self.data.pop()

    def top(self) -> 'int':
        return self.data[-1][0]

    def getMin(self) -> 'int':
        return self.data[-1][1]
        
def __init__(self):
    """
    initialize your data structure here.
    """
    self.stack= []

def push(self, x):
    """
    :type x: int
    :rtype: nothing
    """
    if not self.stack:self.stack.append((x,x)) 
    else:
       self.stack.append((x,min(x,self.stack[-1][1])))

def pop(self):
    """
    :rtype: nothing
    """
    if self.stack: self.stack.pop()

def top(self):
    """
    :rtype: int
    """
    if self.stack: return self.stack[-1][0]
    else: return None

def getMin(self):
    """
    :rtype: int
    """
    if self.stack: return self.stack[-1][1]
    else: return None
