#给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#最先想到的暴力解法，感觉代码太长，不简洁，还挺快的，以为会超出时间限制呢
#32ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            row = []
            return row
        if numRows == 1:
            row = []
            row.append([1])
            return row
        elif numRows == 2:
            row = []
            row.append([1])
            row.append([1,1])
            return row
        else:
            row = []
            row.append([1])
            row.append([1,1])
            for i in range(2, numRows):
                temp = []
                temp.append(1)
                for j in range(1, i):
                    temp.append(row[i-1][j-1]+row[i-1][j])
                temp.append(1)
                row.append(temp)
            return row
       
        
#官方解题方法，思路相同，代码很简洁优美,尤其是学到了[None for _ in range(i)]定义长度为i的空列表
#20ms  99.96%
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0] = 1
            row[-1] = 1
            for j in range(1, len(row)-1):
                row[j] = triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(row)
        return triangle
                    