#给定两个数组，编写一个函数来计算它们的交集。
'''
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
'''
#执行用时 :224 ms, 在所有 Python3 提交中击败了5.06%的用户

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []*len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    a.append(nums1[i])
                    nums2.pop(j)
                    break
        return a