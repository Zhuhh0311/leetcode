#235. 二叉搜索树的最近公共祖先
'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。

示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
'''
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:

            # Value of current node or parent node.
            parent_val = node.val

            if p_val > parent_val and q_val > parent_val:    
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node
'''
思想：假设根结点为root，其中给定的两个结点分别为A和B，它们分别都不为null。如果当前结点p为null，那么直接返回null，如果当前结点p是给定的结点中的其中一个结点，
那么直接返回当前结点p(如果p是根结点，程序一次就返回了，下面的递归也不会出现)。如果当前节点不是A和B中的一个，那么需要分别去查找p的左右子树，
看看是否包含A或者B，查询左右子树后，如果查询左子树和查询右子树的结果都不为null，说明当前结点p就是最近的公共祖先。否则，如果查询左子树结果为null，那么返回查询右子树的结果。反之，返回查询左子树的结果。
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q: return None
        if root.val == p.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: return root
        if left == None: return right
        else: return left


#p,q的公共祖先的值一定介于p,q 之间（闭区间）
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0: root = (root.left, root.right)[p.val > root.val]
        return root
