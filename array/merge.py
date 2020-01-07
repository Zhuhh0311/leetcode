#给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#说明:初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
#     你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

#使用一种笨方法，合并数组之后全部重排，代码是自己写的没参考大佬的，居然通过了好开心
#执行用时 :56 ms, 在所有 Python3 提交中击败了19.86%的用户; 内存消耗 :12.8 MB, 在所有 Python3 提交中击败了99.39%的用户
#时间复杂度 : O((n + m)\log(n + m))； 空间复杂度 : O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        for i in range(m+n):
            for j in range(m+n-i-1):
                if nums1[j]>nums1[j+1]:
                    a = nums1[j+1]
                    nums1[j+1] = nums1[j]
                    nums1[j] = a
#官方解法 60ms
#时间复杂度 : O(n + m)；空间复杂度 : O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1
        
        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] =  nums1[p1]
                p1 -= 1
            p -= 1
        
        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]

		
#使用python内置函数sort() 32ms执行用时 :32 ms, 在所有 Python3 提交中击败了98.57%的用户
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()