#编写一个函数来查找字符串数组中的最长公共前缀。
#如果不存在公共前缀，返回空字符串 ""。
#执行用时 :32 ms, 在所有 Python3 提交中击败了89.94%的用户, 内存消耗 :13.2 MB, 在所有 Python3 提交中击败了53.26%的用户
#照着题解抄的，自己写的漏洞太多，忽略了很多情况
#Python 特性，取每一个单词的同一位置的字母，看是否相同。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
        
        
#取一个单词 s，和后面单词比较，看 s 与每个单词相同的最长前缀是多少！遍历所有单词       
#48 ms, 击败了27.12%      
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res
        
#按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。






        