#226. 翻转二叉树
'''
翻转一棵二叉树。

示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归
#时间复杂度O(n),空间复杂度O(h) # h为树的深度
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def reverse(node):
            if node:
                node.left, node.right = node.right, node.left
                reverse(node.left)
                reverse(node.right)
        reverse(root)
        return root
		
		
#迭代
#时间O(n), 空间复杂度是 O(n)，即使在最坏的情况下，也就是队列里包含了树中所有的节点。对于一颗完整二叉树来说，叶子节点那一层拥有 [n/2] = O(n)个节点
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: 
        if root == None: return None
        queue = [root]
        while queue:
            r = queue.pop(0)
            r.left, r.right = r.right, r.left
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        return root


