'''
有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。
如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。
给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。
对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 
'''
'''
示例：
输入："(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
'''

#1021. 删除最外层的括号
class Solution(object):
    def removeOuterParentheses(self, S):
        target = ''
        count, i = 1, 1
        while i < len(S):
            if S[i] == "(":
                count += 1
            else:
                count -= 1
            if count == 0:
                i += 2
                count += 1
                continue
            target += S[i]
            i += 1
        return target
        
#双指针法，p表示左括号的位置，q表示右括号的位置
#感觉看起来不如上一种方法好理解
class Solution(object):
    def removeOuterParentheses(self, S):
        target = ''
        count, p, q = 0, 0, 0
        while q < len(S):
            count += 1 if S[q] == '(' else -1
            if count == 0:
                S = S[0:p] + S[p+1:q] + S[q+1:] 
                q = q-1
                p = q
                continue
            q += 1
        return S


#利用栈，左括号入栈，当栈的长度大于1，记录当前左括号，碰到右括号时，对应左括号出栈，若此时栈长度不为0，则应记录当前右括号。		
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        #利用栈
        result = ''
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
                if len(stack) > 1:
                    result += s
            else:
                stack.pop()
                if len(stack) != 0:
                    result += s
        return result
        
