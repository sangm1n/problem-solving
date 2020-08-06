"""
Implement Stack using Queues

Implement the following operations of a stack using queues.
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.
"""
from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == '__main__':
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())
