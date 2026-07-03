class MinStack:

    def __init__(self):
        # create main stack
        # create min_stack to track current minimum at each level
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # push value into main stack
        self.stack.append(val)

        # if min_stack is empty, val is the current minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # store the smaller value between val and current minimum
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # remove top from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # return top value from main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # return current minimum
        return self.min_stack[-1]
        
