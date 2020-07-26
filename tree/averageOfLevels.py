#637. 二叉树的层平均值
'''
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#与上一道层序遍历很像
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = []
        cur = [root]
        while cur:
            next_node = []
            i, ans = 0, 0
            for c in cur:
                if c:
                    ans += c.val
                    i += 1
                    next_node.extend([c.left, c.right])
            if i:
                queue.append(ans / i)
            cur = next_node
        return queue


