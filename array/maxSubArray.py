#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#想好了该怎么做却一直写不出来代码，以为自己的想法多好，结果这其实是最暴力的算法，艰难的写出来却一直报错，不知道为啥错了，先保存一下代码，以后再来找错
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums
        com = nums
        for i in range(len(nums)-1):
            sums[i+1] = nums[i+1] + sums[i]
        com[0] = max(sums)
        i=0
        while i < len(nums)-1:
            for j in range(len(nums)-i-1):
                sums[j] = sums[j+1] - nums[i]
            print(sums)
            sums = sums.pop()
            print(sums)
            i+=1
            com[i+1] = max(sums)
           
        return max(com)
'''
动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 ans
如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
'''		
#正确解法   68ms;13.3MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sums = 0
        for i in range(len(nums)):
            if sums > 0:
                sums += nums[i]
            else:
                sums  = nums[i]
            ans = max(ans, sums)
        return ans
		
#更简洁的写法 96ms, 13.4MB	
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i-1], 0)
        return max(nums)
		
#还可以使用分治法来解决问题