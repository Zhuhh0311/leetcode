#104. 二叉树的最大深度
'''

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
'''




#时间复杂度：我们每个结点只访问一次，因此时间复杂度为 O(N)，其中 N 是结点的数量。
#空间复杂度：在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N 次（树的高度），因此保持调用栈的存储将是 O(N)。
#但在最好的情况下（树是完全平衡的），树的高度将是log(N)。因此，在这种情况下的空间复杂度将是O(log(N))。
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
			
#深度优先搜索 depth first search
#DFS与BFS有两点不同：最后得到的深度不一定是最大深度，所以要用max判断；DFS（先序遍历）节点右孩子先入栈，左孩子再入栈`			
class Solution:
    def maxDepth(self, root: TreeNode) -> int:    
        # DFS
        if root is None:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            cur_dep, node = stack.pop()
            depth = max(depth, cur_dep)
            if node.right:
                stack.append((cur_dep+1,node.right))
            if node.left:
                stack.append((cur_dep+1,node.left))
        return depth

#BFS，breath first search层次遍历最后得到的深度就是最大的深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # BFS
        if root is None:
            return 0
        queue = [(1, root)]
        while queue:
            depth, node = queue.pop(0)
            if node.left:
                queue.append((depth+1,node.left))
            if node.right:
                queue.append((depth+1,node.right))
        return depth

