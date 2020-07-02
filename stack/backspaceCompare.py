#844. 比较含退格的字符串
#给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#注意：如果对空文本输入退格字符，文本继续为空。
'''
示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
'''
		
#自己的想法，将两个字符串都重构，然后比较是否相等，使用栈存储重构后的结果
#思路没问题，但是代码冗余
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s, stack_t = [], []
        for i in S:
            if stack_s:
                if i == '#':
                    stack_s.pop()
                else:
                    stack_s.append(i)
            else:
                if i != '#':
                    stack_s.append(i)
        for i in T:
            if stack_t:
                if i == '#':
                    stack_t.pop()
                else:
                    stack_t.append(i)
            else:
                if i != '#':
                    stack_t.append(i)
        return stack_s == stack_t

		
#同样的思路，看人家官方题解多简洁明了。。。		
#时间复杂度O(M+N),空间复杂度也是O(M+N)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(S):
            ans = []
            for s in S:
                if s != '#':
                    ans.append(s)
                elif ans:
                    ans.pop()
			#return ans 这一步直接比较ans不join也可以，join的话与题目示例的输出相同，均为str
            return ''.join(ans)
        return build(S) == build(T)
		
#官方题解给出的另一种方法，反向遍历
#yield  是个知识点
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
