#在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
#返回重复了 N 次的那个元素。
'''
示例 1：

输入：[1,2,3,3]
输出：3
'''
#总觉得这个暴力法还蛮快的。。。
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] == A[j]:
                    return A[i]
  
  
#官方题解，只需考虑长度为4的子序列，子序列中出现重复元素则直接返回
class Solution(object):
    def repeatedNTimes(self, A):
        for k in xrange(1, 4):#这里的xrange报错
            for i in xrange(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]  
					
					
#利用set,如果set中出现过，则直接返回其值				
class Solution(object):
    def repeatedNTimes(self, A):
        a = set()#集合是无序的不重复的元素集，类似数学中的集合，可进行逻辑运算和算术运算。
        for i in A:
            if i not in a:
                a.add(i)
            else:
                return i
