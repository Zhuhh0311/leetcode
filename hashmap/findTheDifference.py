#389. 找不同

'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：
e
'''
#最近做集合的题做多了，一看到题想到的都是set......
#下面做法只有元素不重复时可以，当s=["a"], t=["aa"]时执行出错
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S, T = set(s), set(t)
        return list(T - S)[0]
		
#自己的想法	
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S = collections.Counter(s)
        T = collections.Counter(t)
        for i in T:
            if S.get(i) != T[i]:
                return i
				
'''
map是python内置函数，会根据提供的函数对指定的序列做映射。
map()函数的格式是：map(function,iterable,...)
第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。
'''
#利用ASCII码，ord()函数以字符作为参数，返回其ASCII值，其配对函数为chr()函数
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        S = map(ord, s)
        T = map(ord, t)
        return chr(sum(T)-sum(S))
		
#用异或操作（当两位相同时为0，不同时为1）
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tmp = s + t
        res = ord(tmp[0])
        for i in tmp[1:]:
            res ^= ord(i)
        return chr(res)
        