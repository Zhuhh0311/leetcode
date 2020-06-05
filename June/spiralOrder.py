#面试题29. 顺时针打印矩阵
#输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
'''
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
'''
#看到题的第一想法就是下面代码的想法，但是写了几行觉得太麻烦了，怕不对，就去看了题解
#自己把想法转化为代码的能力还是差的远啊
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        rows, columns = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1, 0, columns-1
        res = []
        while left <= right and top <= bottom:
            for column in range(left, right+1):
                res.append(matrix[top][column])
            for row in range(top+1, bottom+1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right-1, left-1, -1):
                    res.append(matrix[bottom][column])
                for row in range(bottom-1, top, -1):
                    res.append(matrix[row][left])
            top += 1
            left += 1
            bottom -= 1
            right -= 1
 
       return res

#在评论中看到的神仙解法,绝了。。。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            print (res)
			print(*matrix)
            matrix = list(zip(*matrix))[::-1]
            print (matrix)
        return res
#*matrix的作用是把列表的最外一层去掉[[1,2,3],[4,5,6]]变成[1,2,3],[4,5,6]
'''
res, *matrix, matrix对应值
[1, 2, 3, 4]
[5, 6, 7, 8] [9, 10, 11, 12]
[(8, 12), (7, 11), (6, 10), (5, 9)]
[1, 2, 3, 4, 8, 12]
(7, 11) (6, 10) (5, 9)
[(11, 10, 9), (7, 6, 5)]
[1, 2, 3, 4, 8, 12, 11, 10, 9]
(7, 6, 5)
[(5,), (6,), (7,)]
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5]
(6,) (7,)
[(6, 7)]
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

'''

        