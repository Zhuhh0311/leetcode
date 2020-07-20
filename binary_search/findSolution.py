#1237. 找出给定方程的正整数解
'''
给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。
给定函数是严格单调的，也就是说：
f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)
'''

#没看懂题意，抄的
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans,x,y = [],1,1000
        while x <= z and y >= 1:
            res = customfunction.f(x,y)
            if res < z:
                x += 1
            elif res > z: 
                y -= 1
            if res == z:
                ans.append([x,y])
                x += 1
                y -= 1
        return ans
