#给定一个Excel表格中的列名称，返回其相应的列序号。
'''
例如：
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

#执行用时 :44 ms, 在所有 Python3 提交中击败了28.00%的用户
class Solution:
    def titleToNumber(self, s: str) -> int:
        az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        az_list = list(az)
        az_dict = dict(zip(az_list, range(1,27)))
        sum = 0
        for i in range (len(s)):
            sum += 26 ** (len(s)-i-1) * az_dict[s[i]] 
        return sum
#使用ord(x)-64直接代替大写英文字母的值
#32ms      
class Solution:
    def titleToNumber(self, s: str) -> int:
        # return ord("A")  # A = 65
        sum = 0
        for i in range(len(s)):
            sum += (ord(s[i]) - 64) * 26 ** (len(s)-i-1)
        return sum