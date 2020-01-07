#给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#你可以假设数组中无重复元素。

#1.觉得这个题目相对简单一些，比较快写了出来，但是第一遍提交忽略了target大于nums中所有值的情况
#56ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i<len(nums):
            if nums[i] == target:
                return i
                break
            elif nums[i] < target:
                i += 1
            else:
                return i
        if i == len(nums):
            return i
			
#精简了一下代码  92ms 不知为何时间反倒增加了，感觉是网络的原因
class Solution: 
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i<len(nums):
            if nums[i] < target:
                i += 1
            else:
                return i
                break
        if i == len(nums):
            return i
			
#还有更精简的一行代码出结果。。。 76ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([arg for arg in nums if arg < target])
		
#使用二分法来计算，96ms,搞不懂，咋这么玄乎
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        l = 0
        r = n - 1
        while(l <= r):
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return l

            