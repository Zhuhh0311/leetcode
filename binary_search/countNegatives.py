#1351. 统计有序矩阵中的负数
'''
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
请你统计并返回 grid 中 负数 的数目。

示例 1：
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

示例 4：
输入：grid = [[-1]]
输出：1
'''

#二分查找，时间复杂度O(mlogn),空间O(1)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            left = 0
            right = n-1
            while left <= right:
                mid = (left+right) // 2
                if grid[i][mid] >= 0:
                    left = mid+1
                else:
                    right = mid-1
            ans += n - left
        return ans
		
#日常投机取巧。。。
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return str(grid).count('-')
		
'''
倒序遍历
考虑方法三发现的性质，我们可以设计一个更简单的方法。考虑我们已经算出第 ii 行的从前往后第一个负数的位置 pos_ipos 
i，那么第 i+1的时候，pos_{i+1}的位置肯定是位于 [0,pos_i] 中，所以对于第 i+1 行我们倒着从 pos_i循环找 pos_{i+1}即可，这个循环起始变量是一直在递减的
'''
#也可以使用暴力搜寻
#当两层循环时，可以考虑当碰到负数时，跳出循环
