#101. 对称二叉树
'''
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#自己写的，算是迭代的方法吧，感觉受层次遍历那道题影响之后，解题思路都往那上靠了...
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        cur = [root]
        while cur:
            cur_node_val = []
            next_node = []
            for c in cur:
                if c:
                    cur_node_val.append(c.val)
                    next_node.extend([c.left, c.right])
                else:
                    cur_node_val.append(None)      
            cur = next_node
			#判断是否为回文数组这里可以简化成 if cur_node_cal != cur_node_val[::-1]: return False
            for i in range(len(cur_node_val) // 2):
                if cur_node_val[i] != cur_node_val[len(cur_node_val)-1-i]:
                    return False
			#
        return True
		

#题解中给的递归解法
#思路：当节点为空时，是对称的树，当只有一个节点时，也是对称的，否则当左右子树均为对称的时，才对称 左右子树对称则要求左子树的左 有右子树的右，以及左子树的右与右子树的左对称
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def sym(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return sym(node1.left, node2.right) and sym(node1.right, node2.left)
        return sym(root.left, root.right)
        
        
        
        
        