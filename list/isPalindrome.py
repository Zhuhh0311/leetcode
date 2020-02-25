#判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
'''

#之前好像做过类似的，代码自己写的
#112ms,12.4%
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        while x > 0:
            a = x % 10
            l.append(a)
            x = x // 10
        for i in range(len(l)//2):
            if l[i] != l[len(l)-1-i]:
                return False
        return True
        
#参照官方题解写的python 版本
#72ms
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x = x // 10
        return x == rev or x == rev // 10