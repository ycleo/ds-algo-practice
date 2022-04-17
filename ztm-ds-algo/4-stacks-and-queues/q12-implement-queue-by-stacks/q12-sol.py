# // LeetCode 232.
# // https://leetcode.com/problems/implement-queue-using-stacks/

# MyQueue:   back  [3, 8, 1]  front

# stack1:    front [  ] back
# stack2:    back  [  ] front

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  

    def peek(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2[-1]
        if len(self.stack1) > 0:
            return self.stack1[0]
        return None

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()