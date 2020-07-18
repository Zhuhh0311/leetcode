#441. 排列硬币
'''
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
给定一个数字 n，找出可形成完整阶梯行的总行数。
n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.
'''
#使用开根号函数sqrt, pow()函数可以实现开任意次方
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8*n + 1)-1) // 2)
		
#也可以直接0.5次方
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(((8*n + 1) ** 0.5 -1)// 2)
#遍历法，但是执行真的需要好长时间呀。。。		
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1: return n
        sum = 0
        for i in range(1,n+1):
            sum += i
            if sum > n:
                break
        return i - 1
#还可以用二分查找做  定义target=m*(m+1)/2 
'''
形成0行阶梯一共需要0个硬币，形成1行阶梯一共需要1个硬币，形成2行阶梯一共需要3个硬币，形成x行阶梯一共需要 1+2+...+x = (1+x)x/2个硬币。
换句话说，形成0、1、2、3……n 行阶梯需要的硬币数是 [0, 1, 3, 6, ...., (1+n)n/2]，可以看出是一个递增序列。
现在题目问“有n个硬币时，能形成的完整阶梯行数”，抽象后就是“给你一个递增数组 nums，要求你返回 target 的位置，如果 target 不存在就返回距离 target 最近的左侧元素的位置”。
'''