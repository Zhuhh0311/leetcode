#155. 最小栈
'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：
[null,null,null,null,-3,null,0,-2]
'''

#不太接触这种定义多个函数的写法
#下述代码不符合题目 *在常数时间内检索到最小元素的栈* 的要求
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []


    def push(self, x: int) -> None:
        self.s.append(x)


    def pop(self) -> None:
        self.s.pop()


    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return min(self.s)

#构建辅助栈，以空间换时间
#数据栈与辅助栈同步
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.helper = []


    def push(self, x: int) -> None:
        self.s.append(x)
        if len(self.helper) == 0 or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])


    def pop(self) -> None:
        self.s.pop()
        self.helper.pop()


    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return self.helper[-1]
		
#数据栈与辅助栈不同步
#当辅助栈为空时元素需要进栈；当数据栈新进入的元素小于等于辅助栈栈顶元素时，添加到辅助栈中；在出栈时仅当数据栈栈顶与辅助栈栈顶元素相同时才出栈

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.helper = []


    def push(self, x: int) -> None:
        self.s.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        top = self.s.pop()
        if self.helper and self.helper[-1] == top:
            self.helper.pop()


    def top(self) -> int:
        return self.s[-1]


    def getMin(self) -> int:
        return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

