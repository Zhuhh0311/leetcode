#给定一个整数，写一个函数来判断它是否是 3 的幂次方。


#判断n对3取余是否为0，为0则一直继续，否则返回
#执行用时 :96 ms, 在所有 Python3 提交中击败了47.66%的用户
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1
        
#还有几种方法没有列出来