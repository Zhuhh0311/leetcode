#349. 两个数组的交集
#给定两个数组，编写一个函数来计算它们的交集。
'''
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
'''
#时间复杂度O(M+N),空间复杂度O(M+N)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #res = []
        n1 = list(set(nums1))
        n2 = list(set(nums2))
        res = [val for val in n1 if val in n2]
        '''
        for val in n1:
            if val in n2:
                res.append(val)
        '''
        return res
		
#使用内置函数，Python 提供了可用于求交集的 & 运算符
#时间复杂度：一般情况下是 O(m+n)，最坏情况下是 O(m×n) 。
#空间复杂度：最坏的情况是 O(m+n)，数组中的所有元素都不同。


class Solution:
    def intersection(self, nums1, nums2):  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
