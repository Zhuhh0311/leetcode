#110. 平衡二叉树
'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#想直接用函数isBalanced递归，没想好咋做，只能先把每个节点的高度算出来，然后再对每个节点判断其左右子树的高度差是否超过1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node is None: return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1
        if root is None: return True
        cur = [root]
        while cur:
            next_node = []
            for c in cur:
                if c:
                    if abs(height(c.left)-height(c.right)) > 1:
                        return False
                    next_node.extend([c.left, c.right])
            cur = next_node
        return True
#官方题解中自顶向下的递归
#将height函数与解题函数并列写，都使用递归	
class Solution:
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)

#自底向上的递归		
#方法一计算 height 存在大量冗余。每次调用height 时，要同时计算其子树高度。
#但是自底向上计算，每个子树的高度只会计算一次。可以递归先计算当前节点的子节点高度，然后再通过子节点高度判断当前节点是否平衡，从而消除冗余。

#检查子树是否平衡。如果平衡，则使用它们的高度判断父节点是否平衡，并计算父节点的高度。
        
class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]
          
                
        