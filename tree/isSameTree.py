#100. 相同的树
'''
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
'''

#先序遍历的递归算法
#时间复杂度 : O(N)，其中 N 是树的结点数，因为每个结点都访问一次。
#空间复杂度 : 最优情况（完全平衡二叉树）时为O(log(N))，最坏情况下（完全不平衡二叉树）时为 O(N)，用于维护递归栈。
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#层次遍历的非递归算法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        queue = ([(p,q)])
        while queue:
            p, q = queue.pop(0)
            if not check(p,q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True
