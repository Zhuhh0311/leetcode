'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

'''
#自己想的，56ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(list(s))
        b = sorted(list(t))
        return a == b
        #return sorted(a) == sorted(b)
        
#参考题解，使用哈希表
#72ms
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = [0]*26
        for i in range(len(s)):
            alpha[ord(s[i])-ord('a')] += 1
            alpha[ord(t[i])-ord('a')] -= 1
        for i in range(26):
            if alpha[i] != 0:
                return False
        return True