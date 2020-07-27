#538. 把二叉搜索树转换为累加树
#给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
'''
例如：
输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#感觉自己最近陷入固定思维了，总是想用一种遍历方法解决所有树的问题。
#以下写法就是，固定思维的产物，逻辑是没有问题的，但是提交超时了
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None: return 
        queue = []
        cur = [root]
        while cur:
            cur_node_val = []
            next_node = []
            for c in cur:
                if c:
                    cur_node_val.append(c.val)
                    next_node.extend([c.left, c.right])
            cur = next_node
            queue.extend(cur_node_val)
        res = []
        for i in range(len(queue)):
            ans = queue[i]
            for j in range(len(queue)):
                if i != j and queue[j] > queue[i]:
                    ans += queue[j]
            res.append(ans)
        cur = [root]
        while cur:
            next_node = []
            for c in cur:
                if c:
                    c.val = res.pop(0)
                    next_node.extend([c.left, c.right])
            cur = next_node
        return root
	
	
'''
在递归方法中，我们维护一些递归调用过程中可以访问和修改的全局变量。首先我们判断当前访问的节点是否存在，如果存在就递归右子树，递归回来的时候更新总和和当前点的值，然后递归左子树。
如果我们分别正确地递归 root.right 和 root.left ，那么我们就能正确地用大于某个节点的值去更新此节点，然后才遍历比它小的值.

时间复杂度： O(n)
一个二叉树是没有环的，所以 convertBST 对于每个节点来说不会被调用超过 1 次。除去递归调用以外， convertBST 做的工作是常数时间的，所以线性次调用 convertBST 的运行时间是线性时间的。

空间复杂度：O(n)
使用之前的结论 convertBST 会被调用线性次，我们可以知道整个算法的空间复杂度也是线性的。考虑最坏情况，一棵树只有右子树（或者只有左子树），调用栈会一直增长直到到达叶子节点，也就是包含 n 个节点。
'''	
			
class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root
		
'''
一个描述迭代栈的方法就是通过递归的思想。首先我们初始化一个空的栈并把根节点作为当前节点。
然后只要在栈中有未遍历节点或者 node 节点不为空，我们就将当前节点到最右边叶子路径上的点全部压入栈中。这与递归过程中我们总是先走右子树的思路是一致的，这个思路确保我们总是降序遍历所有节点的值。
接下来，我们访问栈顶节点，并考虑它的左子树，这就像我们递归中先遍历当前节点再遍历它的左子树的思路。最后，我们的栈为空并且 node 指向树中最小节点的左孩子 null ，循环结束。
'''

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root


