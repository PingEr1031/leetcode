# https://leetcode-cn.com/problems/implement-queue-using-stacks/
"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
"""


# 使用输入栈 + 输出栈
# 其中输出栈特殊：输出栈不为空直接依次输出，否则将进栈元素全部导入出栈中
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        self.pop()
        p = self.stack_out.pop()
        self.stack_in.append(p)
        return p

    def empty(self) -> bool:
        if self.stack_in or self.stack_out:
            return True
        else:
            return False


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.peek()
    q.pop()
    q.empty()
