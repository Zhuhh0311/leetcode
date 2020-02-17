#一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
#然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。



#自己的直接想法，试运行时就显示超出时间限制
#!!知道问题出在哪里了，不是快乐数时无限循环
class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            a = str(n)
            sum = 0
            for i in range(len(a)):
                sum += int(a[i])**2
            n = sum
        return n == 1
    

#利用集合，判断n是否陷入循环状态
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {1}
        while n not in seen:
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1
        
        
#寻找规律
'''
不是快乐数的数称为不快乐数(unhappy number)，所有不快乐数的数位平方和计算，最后都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环中
已知规律： [1 ~ 4] 中只有 1 是快乐数，[5 ~ ∞] 的数字要么回归到 1 要么回归到 4 或 3
因此仅需在 n > 4 时调用递归
'''


#利用快慢指针
#存疑：这里本想定义一个函数代替str(sum(int(i) ** 2 for i in str(slow这一句，但是运行时显示未定义
class Solution:
    def isHappy(self, n):
        slow = str(n)
        fast = str(sum(int(i) ** 2 for i in str(n)))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in str(slow)))
            fast = str(sum(int(i) ** 2 for i in str(fast)))
            fast = str(sum(int(i) ** 2 for i in str(fast)))
        return fast == '1'

