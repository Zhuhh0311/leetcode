#965. 单值二叉树
'''
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#一开始想在遍历的同时就判断节点的值是否相同，但是没写出来，感觉只能判断出来值不相等的情况，返回True需要所有的值相同
#之后想到先保存遍历结果，再判断是否只由一个值组成 (深度优先搜索)
#时间与空间都是O(n)
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not (root.left or root.right): return True
        self.ans = []
        def dfs(node):
            if node:
                self.ans.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return len(set(self.ans)) == 1
		
#递归 时间O(n),空间O(h),h为树的高度		
'''
一颗树是单值的，当且仅当根节点的子节点所在的子树也是单值的，同时根节点的值与子节点的值相同。
我们可以使用递归实现这个判断的过程。left_correct 表示当前节点的左孩子是正确的，也就是说：左孩子所在的子树是单值的，并且当前节点的值等于左孩子的值。
right_correct 对当前节点的右孩子表示同样的事情。递归处理之后，当根节点的这两种属性都为真的时候，我们就可以判定这颗二叉树是单值的。
'''	
class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
