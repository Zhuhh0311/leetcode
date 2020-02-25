
#给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#自己写的，感觉代码还能精简，之前做过判断3的幂
#32ms, 82.96%
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0:
            return False
        while n > 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True
#简化版本       
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n / 2
        return True
        
#利用位运算 n&(n-1) == 0        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0