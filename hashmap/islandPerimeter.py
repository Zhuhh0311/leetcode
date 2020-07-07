#463. 岛屿的周长
'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例：
输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16
'''
#对于每个方块，只需计算方块上面和左面的边的值，最终将值乘以2便是最终答案
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        pre = 0
        length = len(grid)
        width = len(grid[0])
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        pre += 1
                    if j == 0 or grid[i][j-1] == 0:
                        pre += 1
        return pre * 2
#另一种思路，若方块为陆地，总长+4，如果上边和左边有陆地，分别减去2,（两个陆地重合的话有两条边不能用）	
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        pre = 0
        length = len(grid)
        width = len(grid[0])
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    pre += 4
                    if i-1 >= 0 and grid[i-1][j] == 1:
                        pre -= 2
                    if j-1 >= 0 and grid[i][j-1] == 1:
                        pre -= 2
        return pre