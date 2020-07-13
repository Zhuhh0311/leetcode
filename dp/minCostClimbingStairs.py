#746. 使用最小花费爬楼梯
'''
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
'''
#想了好久的动态规划方法，动态规划方程感觉是没错的，但是在处理开始时选择0，1台阶时会犯错误
#看了官方题解，原来是返回时没有选择dp[n-2],dp[n-1]中的较小值

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1: return cost[0]
        elif n == 2: return min(cost[0], cost[1])
        elif n == 3: return min(cost[1], cost[0]+cost[2])
        else:
            dp = [0] * n
            dp[0] = cost[0]
            dp[1] = min(cost[0],cost[1])
            i = 2
            while i < n:
                dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
                i = i + 1
            return dp[n-1]
#官方题解，空间复杂度O(n),时间复杂度O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        dp = [0 for _ in range(size)]

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, size):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[size - 1], dp[size - 2])
		
#可以优化空间复杂度，用两个变量存储dp[i-1],dp[i-2],然后每一步更新值
#直接改变cost元素值，空间复杂度O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return min(cost[-1],cost[-2])