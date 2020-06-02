#面试题64. 求1+2+…+n
#求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）


#使用递归，用逻辑运算符代替if判断递归结束
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res
		
		
#python之一行解决
class Solution:
    def sumNums(self, n):
        return sum(range(n+1))

