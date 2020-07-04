'''
请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。
'''
#使用辅助栈，利用空间换时间
#s与stack同步（也可以两者不同步）
#问题重复了，反思为什么重复的问题还是不会！
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 
        self.s = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.s or x <= self.s[-1]:
            self.s.append(x)
        else:
            self.s.append(self.s[-1])
            

    def pop(self) -> None:
        self.stack.pop()
        self.s.pop()


    def top(self) -> int:           
        return self.stack[-1]


    def getMin(self) -> int:
        return self.s[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()