#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#有效字符串需满足：
#左括号必须用相同类型的右括号闭合。
#左括号必须以正确的顺序闭合.

#利用栈先进后出的特点
#stack.pop()删除元素，默认为列表最后一位元素，并返回删除的元素本身


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','{':'}','[':']'}
        for stri in s:
            if stri in dic:
                stack.append(stri)
            elif dic[stack.pop()] != stri:
                return False
        if len(stack) == 0:
            return True
#当碰到右括号时，若栈为空，stack.pop()操作会报错，故在栈中预先放入一个'?'元素
#字典中加入？：？是由于dic[stack.pop()]操作需要？元素的value
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: 
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False 
        return len(stack) == 1




