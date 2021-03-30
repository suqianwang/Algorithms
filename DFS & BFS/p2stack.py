"""
Math 560
Project 2
Fall 2020

p2stack.py

Author: Suqian Wang
Date: October 22, 2020
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        return len(self.stack) == self.numElems

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        new_stack = [None for x in range(len(self.stack)*2)]
        for index,value in enumerate(self.stack):
            new_stack[index] = value
        self.stack = new_stack
        return 

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        if(self.isFull()):
            self.resize()
        self.top += 1
        self.stack[self.top] = val
        self.numElems += 1
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        return_val = None
        if not self.isEmpty():
            return_val = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            self.numElems -= 1
        return return_val
