#实现 strStr() 函数。
#给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#当 needle 是空字符串时我们应当返回 0 

#自己的思路，感觉代码有点冗余#执行用时 :40 ms, 在所有 Python3 提交中击败了54.45%的用户内存消耗 :13 MB, 在所有 Python3 提交中击败了57.30%的用户
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        n = len(needle)
        h = len(haystack)
        if h < n:
            return -1
        i = 0
        while i <= h-n:
            if haystack[i:i+n] == needle[:]:
                return i
                break
            else:
                i += 1
        if i == h-n+1:
            return -1
        
        
#使用python内置函数find 
#28ms
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        
#我的想法的代码简化版本，自己对于一些基础的语言知识掌握不够
#28ms
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1



