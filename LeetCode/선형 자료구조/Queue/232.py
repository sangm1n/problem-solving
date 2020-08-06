"""
Implement Queue using Stacks

Implement the following operations of a queue using stacks.
    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.
"""


class MyQueue:
    def __init__(self):
        self.input = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        item = self.input[0]
        self.input = self.input[1:]
        return item

    def peek(self) -> int:
        return self.input[0]

    def empty(self) -> bool:
        return len(self.input) == 0


if __name__ == '__main__':
    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
