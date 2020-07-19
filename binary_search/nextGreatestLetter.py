#744. 寻找比目标字母大的最小字母
'''
给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
在比较时，字母是依序循环出现的。举个例子：
如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'

示例：
输入:
letters = ["c", "f", "j"]
target = "a"
输出: "c"

输入:
letters = ["c", "f", "j"]
target = "k"
输出: "c"
'''

#线性扫描， 时间O(N),空间O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in letters:
            if ord(l) > ord(target):#可以直接使用 if l > target: return l
                return l
        else:
            return letters[0]
			
			
#记录存在的字母  时间O(N),空间O(1)
'''
算法：
我们可以扫描 letters 记录字母是否存在。我们可以用大小为 26 的数组或者 Set 来实现。
然后，从下一个字母（从比目标大一个的字母开始）开始检查一下是否存在。如果有的话则是答案。
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand
'''				
bisect是python内置模块，用于有序序列的插入和查找。

查找： bisect(array, item)
插入： insort(array,item)
'''
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


#二分查找		
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if letters[-1] <= target: return letters[0]
        left = 0
        right = len(letters) - 1
        while left <=right:
            mid = (left+right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        return letters[left]
