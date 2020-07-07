#290. 单词规律
'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true
'''
#时间只击败了百分之5。。。
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split( )
        if len(s) != len(pattern): return False
        m = list(zip(pattern, s))
        for i in range(len(s)):
            for j in range(len(s)):
                if m[i][0] == m[j][0] and m[i][1] != m[j][1] or m[i][0] != m[j][0] and m[i][1] == m[j][1]:
                    return False
        return True
		
#index() 方法返回指定值首次出现的位置。
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        res=str.split()
        return list(map(pattern.index, pattern))==list(map(res.index,res))
#这个方法也太秀儿了！		
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(str.split(" ")) != len(list(pattern)):
            return False
        for l in zip(*set(zip(list(pattern), str.split(" ")))):#*号用于zip的逆过程
            if len(l) != len(set(l)):
                return False
        return True
#建立pattern->str, 与str->pattern的哈希映射，当当前值不在哈希表中则添加，若已存在则比较	其value是否相同
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        hash1, hash2 = {}, {}
        a = str.split(' ')
        if len(pattern) != len(a): return False
        for i in range(len(pattern)):
            if pattern[i] not in hash1:
                hash1.update({pattern[i]: a[i]})
            else:
                if hash1.get(pattern[i]) != a[i]:
                    return False
        for i in range(len(pattern)):
            if a[i] not in hash2:
                hash2.update({a[i]: pattern[i]})
            else:
                if hash2.get(a[i]) != pattern[i]:
                    return False
        return True
            
