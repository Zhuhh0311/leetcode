#1441. 用栈操作构建数组
'''
给你一个目标数组 target 和一个整数 n。每次迭代，需要从  list = {1,2,3..., n} 中依序读取一个数字。

请使用下述操作来构建目标数组 target ：

Push：从 list 中读取一个新元素， 并将其推入数组中。
Pop：删除数组中的最后一个元素。
如果目标数组构建完成，就停止读取更多元素。
题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。

请返回构建目标数组所用的操作序列。

题目数据保证答案是唯一的。

示例 1：
输入：target = [1,3], n = 3
输出：["Push","Push","Pop","Push"]
解释： 
读取 1 并自动推入数组 -> [1]
读取 2 并自动推入数组，然后删除它 -> [1]
读取 3 并自动推入数组 -> [1,3]

'''

#自己做出来的，但是看到题解很少，说是大佬们都不屑于做这道题。。。
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = []
        i = 0
        for j in range(len(target)):
            i += 1
            while target[j] > i:
                t.append("Push")
                t.append("Pop")
                i += 1
            t.append("Push")
        return t
		
#题解中更加简洁的代码，思路是一样的
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        cur = 1
        for i in target:
            if i != cur:
                res.extend(["Push","Pop"] * (i-cur))
            res.append('Push')
            cur = i+1
        return res