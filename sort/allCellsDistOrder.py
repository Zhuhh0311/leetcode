#1030. 距离顺序排列矩阵单元格

'''
给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

示例 2：
输入：R = 2, C = 2, r0 = 0, c0 = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
'''

#还是有很多内容不会啊。。。
#也不知道这种方法算不算桶排序？
#还有BFS和几何法可以解题，但是看起来就好难，还涉及到树，先留着吧。。。
class Solution:
    def allCellsDistOrder(self, R, C, r0, c0):
        dist_list = [[] for i in range(R*C)]
        for r in range(R):
            for c in range(C):
                dist = abs(r0-r) + abs(c0-c)
                dist_list[dist].append([r, c])
        result = []
        for i in dist_list:
            if i:
                result.extend(i)
            else:
                break
        return result