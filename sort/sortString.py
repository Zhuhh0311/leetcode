#1370. 上升下降字符串
'''
给你一个字符串 s ，请你根据下面的算法重新构造字符串：

从 s 中选出 最小 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最小 的字符，且该字符比上一个添加的字符大，将它 接在 结果字符串后面。
重复步骤 2 ，直到你没法从 s 中选择字符。
从 s 中选出 最大 的字符，将它 接在 结果字符串的后面。
从 s 剩余字符中选出 最大 的字符，且该字符比上一个添加的字符小，将它 接在 结果字符串后面。
重复步骤 5 ，直到你没法从 s 中选择字符。
重复步骤 1 到 6 ，直到 s 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 s 中字符重新排序后的 结果字符串 。

示例 3：
输入：s = "leetcode"
输出："cdelotee"
'''




#any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
#元素除了是 0、空、FALSE 外都算 TRUE。
class Solution:
    def sortString(self, s: str) -> str:
        h = [0] * 26
        for ch in s:
            h[ord(ch)-97] += 1
        def appendChar(ret, p):
            if h[p] > 0:
                h[p] -= 1
                ret.append(chr(p + 97))
        def haveChar():
            return any(h[i] > 0 for i in range(26))
        ret = []
        while True:
            if not haveChar():
                break
            for i in range(26):
                appendChar(ret, i)
            for i in range(26):
                appendChar(ret, 25 - i)
        return "".join(ret)
		
#评论区发现了这个题解，与我一闪而过的想法是相同的，可惜我不知道如何去实现它，主要是不知道如何用collections.Counter	来做
class Solution:
    def sortString(self, s: str) -> str:
        chars=collections.Counter(s)
        ans=[]
        signal=0
        while chars:
            group=list(chars)
            group.sort(reverse=signal)
            ans.extend(group)
            chars-=collections.Counter(group)
            signal=1-signal
        return ''.join(ans)
