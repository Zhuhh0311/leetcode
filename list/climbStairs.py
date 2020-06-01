#70. Climbing Stairs
'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
'''
#使用动态规划方法
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = ['']*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
		
#利用斐波那契数列	
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        i = 3
        while i < n+1:
            third = first + second
            first = second
            second = third
            i += 1
        return second