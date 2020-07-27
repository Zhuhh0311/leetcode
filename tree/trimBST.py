#669. 修剪二叉搜索树
'''
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例 1:
输入: 
    1
   / \
  0   2

  L = 1
  R = 2
输出: 
    1
      \
       2
	   
示例 2:
输入: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3
输出: 
      3
     / 
   2   
  /
 1

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None: return  
        while root and (root.val < L or root.val > R):
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left
        if root:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root
		
#官方题解
#当node.val > R，那么修剪后的二叉树必定出现在节点的左边。类似地，当node.val < L，那么修剪后的二叉树出现在节点的右边。否则，我们将会修剪树的两边。
#时间复杂度：O(N)，其中 N 是给定的树的全部节点。我们最多访问每个节点一次。
#空间复杂度：O(N)，即使我们没有明确使用任何额外的内存，在最糟糕的情况下，我们递归调用的栈可能与节点数一样大。
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)


        
