#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#注意你不能在买入股票前卖出股票。
'''
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
'''
#双指针，暴力解法，提交显示超出时间限制
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = []
        for i in range (len(prices)):
            for j in range (i+1, len(prices)):
                if prices[j] - prices[i] > 0:
                    nums.append(prices[j] - prices[i])
        if nums == []:
            return 0
        else:
            return max(nums) 
     
#动态规划方法，min_price存储迄今为止的最小值，max_price存储迄今为止的最大值
#执行用时 :68 ms, 在所有 Python3 提交中击败了86.99%的用户， 内存消耗 :14.3 MB, 在所有 Python3 提交中击败了57.48%的用户
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        max_price = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_price = max(max_price, prices[i]-min_price)
        return max_price  


#给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
#注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        sum = 0
        for i in range(1, len(prices)):
            tmp = max(0, prices[i]-prices[i-1])
            sum += tmp
        return sum        