from collections import deque


class MyStack:

    def __init__(self):
        # self.q1 = []
        # self.q2 = []
        # pop(0)时间复杂度为 O(n)，所以使用双端队列
        self.queue_in = deque()
        self.queue_out = deque()
    def push(self, x: int) -> None:
        """正常压入"""
        self.queue_in.append(x)

    def pop(self) -> int:
        """pop - > 队尾"""
        """     
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个"""
        if self.empty():
            return None
        else:
            for i in range(len(self.queue_in)-1):
                self.queue_out.append(self.queue_in.popleft())
            # queue_out 和 queue_in交换
            self.queue_out, self.queue_in = self.queue_in, self.queue_out
            return self.queue_out.popleft()



    def top(self) -> int:
        """栈顶 - > 队尾"""
        if self.empty():
            return None
        return self.queue_in[0]



    def empty(self) -> bool:
        if self.queue_in or self.queue_in:
            return False
        else:
            return True

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.pop()
    param_4 = obj.pop()
    param_5 = obj.empty()




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()