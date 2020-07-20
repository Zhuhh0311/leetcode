#852. 山脉数组的峰顶索引
'''
我们把符合下列属性的数组 A 称作山脉：
A.length >= 3
存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

示例 1：
输入：[0,1,0]
输出：1
'''
#二分查找
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = left + (right-left) // 2
            print(left,right,mid)
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
            
        return left
		
#库函数		
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))
		
#也可以线性搜索，若递增，则继续扫描，一旦出现递减趋势，则返回值

