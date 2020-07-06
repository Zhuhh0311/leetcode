#1160. 拼写单词
'''
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
返回词汇表 words 中你掌握的所有单词的 长度之和。

示例 1：
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
'''


#官方题解
#时间复杂度：O(n)，其中 n 为所有字符串的长度和。我们需要遍历每个字符串，包括 chars 以及数组 words 中的每个单词。
#空间复杂度：O(S)，其中 S 为字符集大小，在本题中 S 的值为 26（所有字符串仅包含小写字母）。
#程序运行过程中，最多同时存在两个哈希表，使用的空间均不超过字符集大小 S，因此空间复杂度为 O(S)。
'''
for......else......的执行顺序为：
当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，没有则继续执行后续代码；
如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码
'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for s in word:
                if chars_cnt[s] < word_cnt[s]:
                    break
            else:
                ans += len(word)
        return ans


#优美简洁的代码，pythonic
#all() 函数(Python内置函数)用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
#元素除了是 0、空、None、False 外都算 True。
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        cnt = collections.Counter(chars)
        for w in words:
            c = collections.Counter(w)
            if all([c[i] <= cnt[i] for i in c]):
                ans += len(w)
        return ans
