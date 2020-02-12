#给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#注意事项：您可以假定该字符串只包含小写字母。

#这个思路想到了，但是没有实现
#执行用时 :156 ms, 在所有 Python3 提交中击败了36.01%的用户
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # build hash map : character and how often it appears
        count = collections.Counter(s)#python中的类似于计算器的作用
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1

