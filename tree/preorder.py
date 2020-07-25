#589. N叉树的前序遍历
#给定一个 N 叉树，返回其节点值的前序遍历。
#前序遍历首先访问根结点然后遍历左子树，最后遍历右子树。在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#递归，终于自己写出了传说中的简单的递归写法。。。
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return 
        def dfs(node):
            self.ans.append(node.val)
            for c in node.children:
                dfs(c)
        self.ans = []
        dfs(root)
        return self.ans
		

#自己写的迭代
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return  
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            for c in reversed(node.children):
                stack.append(c)
            ans.append(node.val)
        return ans

#官方题解中的迭代解法		
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])#主要差别在这一行
                
        return output

