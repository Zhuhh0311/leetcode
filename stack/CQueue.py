#剑指 Offer 09. 用两个栈实现队列
#用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
#(若队列中没有元素，deleteHead 操作返回 -1 )



class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if len(self.stack1) == 0:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        tmp = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return tmp

#一个栈负责进，另一个负责出
#出栈想法比较巧妙，当out不空时，删除其最后的元素，当out为空，in也为空时，返回-1，当out为空但是in不空时，将in的元素出栈，放到out中。代码思路都很简洁
#添加元素时间复杂度为O(1),删除为O(N),空间复杂度为O(N)
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []


    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)


    def deleteHead(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        if not self.stack_in:
            return -1
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

