#617. 合并二叉树 
'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
示例 1:
输入: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
输出: 
合并后的树:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
'''

'''
and的规则如下：
and运算时,从左到右演算表达式的值。0, '', [], {}, None在布尔表达式环境下为假，其他任何东西都为真
如果and运算中，所有的值都为真，那么and返回最后一个值。如：'a' and 'b'
如果某个值为假，那么and立即返回该假值（短路运算），如：'' and 'b'
or的规则如下:
从左到右演算
如果有一个值为真，立即返回该值
所有所有的值都为假，返回最后一个假值
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)

        return t1 or t2
		
		
#迭代		
class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""	
	# 如果 t1和t2中，只要有一个是null，函数就直接返回
		if not (t1 and t2):
			return t2 if not t1 else t1
		queue = [(t1,t2)]
		while queue:
			r1,r2 = queue.pop(0)
			r1.val += r2.val
			# 如果r1和r2的左子树都不为空，就放到队列中
			# 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
			if r1.left and r2.left:
				queue.append((r1.left,r2.left))
			elif not r1.left:
				r1.left = r2.left
			# 对于右子树也是一样的
			if r1.right and r2.right:
				queue.append((r1.right,r2.right))
			elif not r1.right:
				r1.right = r2.right
		return t1