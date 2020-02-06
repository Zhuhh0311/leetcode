#给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

#对于字符串的相关代码不熟悉，没有思路，此题是按照答案抄下来的
#执行用时 :40 ms, 在所有 Python3 提交中击败了97.76%的用户，内存消耗 :13.1 MB, 在所有 Python3 提交中击败了55.39%的用户
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':3, 'IX':8, 'XL':30, 'XC':80, 'CD':300, 'CM':800}
        sums = 0
        t = 0
        for i, n in enumerate(s):
            t = d.get(s[max(0,i-1):i+1], d[n])
            sums += t
        return sums

#52ms       
class Solution:
    def romanToInt(self, s: str) -> int:
        roma_nums = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        num = 0
        for i in range(len(s)-1):
            if roma_nums[s[i]]>=roma_nums[s[i+1]]:
                num += roma_nums[s[i]]
            else:
                num -= roma_nums[s[i]]
        last_num = s[len(s)-1]
        num = num + roma_nums[last_num]
        return num

        