#给定一个整数 n，返回 n! 结果尾数中零的数量。

#自己的想法：有一个5就多一个0，然后直接用n除了5，但是忽略了25里面有两个因子5
class Solution:
    def trailingZeroes(self, n: int) -> int:
		a = (n - n % 5) // 5
		return a

#参看题解后的改动版
#执行用时 :24 ms, 在所有 Python3 提交中击败了98.03%的用户
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 1:
            count += n // 5
            n = n // 5
        return count