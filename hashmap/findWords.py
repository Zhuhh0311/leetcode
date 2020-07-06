'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。

示例：
输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = 'qwertyuiopQWERTYUIOP'
        l2 = 'asdfghjklASDFGHJKL'
        l3 = 'zxcvbnmZXCVBNM'
        l1, l2, l3 = set(l1), set(l2), set(l3)
        final = []
        for i in range(len(words)):
            s = set(words[i])
            if  s&l1 == s or s&l2 == s or s&l3 == s:
                final.append(words[i])
        return final
		
		
class Solution(object):
    def findWords(self, words):
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx <= set1 or setx <= set2 or setx <= set3:#集合之间比较大小，即<=表示子集关系
                res.append(i)
        return res


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        T = []
        list1 = list(set('qwertyuiop'))
        list2 = list(set('asdfghjkl'))
        list3 = list(set('zxcvbnm'))
        def match(list0, str1):
            str1 = list(set(str1.lower()))
            for i in range(len(str1)):
                if str1[i] not in list0:
                    return False
            return True
        for i in range(len(words)):
            if match(list1, words[i]) == True or match(list2, words[i]) == True or match(list3, words[i]) == True:
                T.append(words[i])
        return T
