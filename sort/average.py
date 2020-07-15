#1491. 去掉最低工资和最高工资后的工资平均值
'''
给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。
请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

示例 1：
输入：salary = [4000,3000,1000,2000]
输出：2500.00000
解释：最低工资和最高工资分别是 1000 和 4000 。
去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500
'''
#sort()时间复杂度为O(nlog(n))!!!!故应该用最后一种方法
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop()
        return sum(salary) / len(salary)
#减少了两个删除操作，应该会节省些时间吧
#在做时忽略了除数加括号，一直写成return a / n-2 ，低级错误，不应该！！ 	
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        a = sum(salary) - salary[0] - salary[n-1]
        return a / (n-2)
#还可以省掉排序，直接找最大最小值	
#时间复杂度：O(n)。选取最大值、最小值和求和的过程的时间代价都是 O(n)，故渐进时间复杂度为 O(n)。
#空间复杂度：O(1)。这里只用到了常量级别的辅助空间。
class Solution:
    def average(self, salary: List[int]) -> float:
        maxValue = max(salary)
        minValue = min(salary)
        total = sum(salary) - maxValue - minValue
        return total / (len(salary) - 2)