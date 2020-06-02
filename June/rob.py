#198. House Robber
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight 
without alerting the police.

'''

#使用动态规划来做！！！
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]
        first, second = nums[0], max(nums[0],nums[1])
        for i in range(2,size):
            first, second = second, max(first + nums[i], second)
        return second