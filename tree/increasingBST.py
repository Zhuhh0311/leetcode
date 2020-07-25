#897. 递增顺序查找树
#给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
'''
示例 ：

输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#自己的想法，将树中序遍历得到的结果存到ans中，然后构造新的树
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = []
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans.append(node.val)
                dfs(node.right)
        dfs(root) 
        a = TreeNode(self.ans[0])
        tn = a
        i = 1
        while i < len(self.ans):
            tn.right = TreeNode(self.ans[i])
            tn = tn.right
            i += 1
        return a
#官方题解
#我们在树上进行中序遍历，就可以从小到大得到树上的节点。我们把这些节点的对应的值存放在数组中，它们已经有序。接着我们直接根据数组构件题目要求的树即可。 
#时间O(n),空间O(n)
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right
		
#和方法一类似，我们在树上进行中序遍历，但会将树中的节点之间重新连接而不使用额外的空间。具体地，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子。
#时间O(n),空间O(h),h为树的高度
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right




