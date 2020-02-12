#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#说明：本题中，我们将空字符串定义为有效的回文串。

#自己写的，但是运行时间很慢
#执行用时 :56 ms, 在所有 Python3 提交中击败了59.97%的用户

class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(e for e in s if e.isalnum())
        i = 0
        while i < len(a)//2:
            if a[i].lower() == a[len(a)-i-1].lower():
                i += 1
            else:
                return False
        if i == len(a)//2:
            return True
            
#执行用时 :52 ms  
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > -1 and not s[j].isalnum():
                j -= 1
            if i > j:
                return True
            if s[i].upper() != s[j].upper():
                return False
            else:
                i += 1
                j -= 1
        return True
