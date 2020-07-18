#367. 有效的完全平方数
'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
说明：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入：16
输出：True
'''



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        left = 1#这里可以直接从2开始
        right = num // 2
        while left <= right:
            mid = (left+right) // 2#又忘了可以left+(right-left)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

#牛顿迭代法  f(x) = x * x - num , 从近似值开始逼近f(x)的根		
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        x = num // 2
        while x * x > num:
            x = (x + num//x) // 2
        return x * x == num
		
#等差数列  1,3,5,7,9 ......,2n-1其和为n^2
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0