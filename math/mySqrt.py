#实现 int sqrt(int x) 函数。
#计算并返回 x 的平方根，其中 x 是非负整数。
#由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

#挨个试，提交显示超出时间限制
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        else:
            for i in range(0,x//2 + 1):
                if i**2 <= x and (i+1)**2 > x:
                    return i
                    
#二分法查找
#执行用时 :40 ms, 在所有 Python3 提交中击败了72.34%的用户
class Solution:
    def mySqrt(self, x: int) -> int:
        # 为了照顾到 0 把左边界设置为 0
        left = 0
        # 为了照顾到 1 把右边界设置为 x // 2 + 1
        right = x // 2 + 1
        while left < right:
            # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            mid = left + (right - left + 1) // 2
            #mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        # 因为一定存在，因此无需后处理
        return left    


#还可以使用牛顿法来解        