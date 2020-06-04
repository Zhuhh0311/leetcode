#581. 最短无序连续子数组
#给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#你找到的子数组应是最短的，请输出它的长度

#这个做法没有考虑数组已经排好序的情况，并且在写代码的时候没弄好break的关系
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != n[i]:
                a = i
                break
        for i in reversed(range(len(nums))):
            if nums[i] != n[i]:
                b = i
                break
        return b-a+1
		
#考虑排好序的情况	
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = sorted(nums)
        if n == nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != n[i]:
                a = i
                break
        for i in reversed(range(len(nums))):
            if nums[i] != n[i]:
                b = i
                break
        return b-a+1 
 
 
#简化后的代码
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = []
        n = sorted(nums)
        if n == nums:
            return 0
        for i in range(len(nums)):
            if nums[i] != n[i]:
                a.append(i)
        c = a[len(a)-1] - a[0] + 1
        return c
#题解里的神仙Python算法
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return len(diff) and max(diff) - min(diff) + 1
		
#还可以利用栈来解决问题