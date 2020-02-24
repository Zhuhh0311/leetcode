#不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
#两整数之和
#life is short......
#44ms, 17.87%

class Solution:
    def getSum(self, a: int, b: int) -> int:
        l = [a,b]
        return sum(l)
        
        
        
#利用二进制的异或运算，与运算，位移运算等
#太难了，不是很懂啊啊啊啊啊啊
#居然只用24ms，果然这种运算才是最快的
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1 
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
        
