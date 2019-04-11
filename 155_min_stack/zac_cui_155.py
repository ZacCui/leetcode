#!/usr/local/bin/python3
'''
	Author: Zac Cui
	Created Date: 2019-04-11 13:03:30
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.stack = []

    def push(self, x: int) -> None:
        if not len(self.stack):
            self.min = x
        else:
            self.min = min(self.min, x)
        self.stack.append(x)
        
    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop(-1)
            if len(self.stack):
                self.min = min(self.stack)

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.stack):
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()