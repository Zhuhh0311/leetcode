'''
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。
'''

'''
示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
'''
#暴力解法：对于nums1的每个元素，在nums2中找到它，假设它的下标为i，那么从第i+1位开始搜索是否存在比它大的，找到就将该值加入记录中，否则加入-1
#
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        for num in nums1:
            i = 0
            while num != nums2[i]:
                i += 1
			i += 1 #加上这一行可以减少重复运算
            while i < len(nums2):
                if num < nums2[i]:
                    res.append(nums2[i])
                    break
                i += 1
            if i == len(nums2): res.append(-1)
        return res

#使用单调栈解决,时间复杂度O(M+N),M,N分别为nums1,nums2数组的长度，空间复杂度0(N)，在遍历nums2时需要使用栈和哈希映射来储存临时结果。
'''
我们可以忽略数组 nums1，先对将 nums2 中的每一个元素，求出其下一个更大的元素。随后对于将这些答案放入哈希映射（HashMap）中， 
再遍历数组 nums1，并直接找出答案。对于 nums2，我们可以使用单调栈来解决这个问题。 
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, a = list(), list()
        hashmap = dict()
        for i in nums2:
            while stack and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        for i in nums1:
            a.append(hashmap.get(i, -1))
        return a 