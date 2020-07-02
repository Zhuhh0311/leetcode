#给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。请返回 nums 的动态和。
'''
示例 3：
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
'''
#最先想到的方法，暴力,提交显示此方法较慢
#修改了传来的nums数组
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        return nums
		
#和上一种方法所需时间差不多
#创建了一个新数组保存结果，不改变nums数组的值
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range (len(nums)):
            result.append(sum(nums[0:i+1]))
        return result