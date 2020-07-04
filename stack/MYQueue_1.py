#面试题 03.04. 化栈为队

#实现一个MyQueue类，该类用两个栈来实现一个队列。
'''
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

'''


#这道题重复了
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack_out:
            return self.stack_out.pop()

        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack_out:
            return self.stack_out[-1]
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_in) == 0 and len(self.stack_out) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()