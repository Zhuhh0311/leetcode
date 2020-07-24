#590. N叉树的后序遍历
'''
给定一个 N 叉树，返回其节点值的后序遍历。
左右根
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

#都说递归很简单，但是我还是没自己写出来。。。。
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(node):
            if not root: return 
            for n in node.children:
                helper(n)
            self.ans.append(node.val)

        self.ans = []
        helper(root)
        return self.ans
		
		
		
#迭代方法
#时间复杂度：O(M)，其中 MM是 N 叉树中的节点个数。每个节点只会入栈和出栈各一次。
#空间复杂度：O(M)。在最坏的情况下，这棵 N 叉树只有 2 层，所有第 2 层的节点都是根节点的孩子。将根节点推出栈后，需要将这些节点都放入栈，共有 M - 1个节点，因此栈的大小为 O(M)。
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return  
        stack, output = [root], []
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
            for c in node.children:
                stack.append(c)
        return output[::-1]
        

       
