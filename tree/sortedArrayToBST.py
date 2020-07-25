#108. 将有序数组转换为二叉搜索树
'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

'''







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#时间O(n), n为数组的长度，数组的每个元素只访问一次
#空间O(logn),空间复杂度主要取决于递归栈的深度
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        else:
            n = len(nums) // 2
            tn = TreeNode(nums[n])
            nums1 = nums[0:n]
            nums2 = nums[n+1:len(nums)]
            tn.left = self.sortedArrayToBST(nums1)
            tn.right = self.sortedArrayToBST(nums2)
        return tn