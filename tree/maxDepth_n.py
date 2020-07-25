#559. N叉树的最大深度
#给定一个 N 叉树，找到其最大深度。
#最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#这道题没做完
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        stack = [(1,root)]
        depth = 0
        while stack:
            cur_depth, root = stack.pop()
            depth = max(cur_depth, depth)
            for c in root.children:
                stack.append((cur_depth+1, c))
        return depth
		
		
#使用递归来做
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
        return max(height) + 1
