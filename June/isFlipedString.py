#面试题 01.09. 字符串轮转
#字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）

#python之一行解决
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1*2
		
#与我自己的想法相同，但是我没有实现。。。哎		
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        count=0
		#我觉得加一个长度是否相等的判断会更好
		#if len(s1) != len(s2):
		#return False
        if s1==s2:
            return True
        for i in s1:
            s1=s1[1:]+s1[0]
            if s1==s2:
                return True
        else:
            return False
        