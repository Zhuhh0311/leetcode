'''
225.用队列实现栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
'''

#使用单队列（list）实现
#方法一：使用一个队列，队列添加元素后，反转前n-1个元素，栈顶元素始终保留在队首
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        #例如：q = [1,2,3,4,5,x],反转后q为[x,1,2,3,4,5],即将X添加为栈顶元素
        self.q.append(x)
        q_length = len(self.q)
        while q_length > 1:
            self.q.append(self.q.pop(0)) #反转前n-1个元素，栈顶元素始终保留在队首
            q_length -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.q)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
        
        
        
#方法二 使用双端队列（deque）实现
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.help = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #popleft()用于collections中，不带参数
        while len(self.data) > 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.data, self.help = self.help, self.data
        return tmp


    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.data) != 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help.append(tmp)
        self.data, self.help = self.help, self.data
        return tmp
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.data)


#第二次做，用两个队列实现，但是代码有些冗余，还是要加油呀~
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        a = self.queue1.pop(0)
        while self.queue2:
            self.queue1.append(self.queue2.pop(0))
        return a


    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))
        a = self.queue1[0]
        self.queue2.append(a)
        self.queue1 = self.queue2
        self.queue2 = []
        return a



    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


