#给定一个整数数组，判断是否存在重复元素。
#如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
'''
一般而言，如果一个算法的时间复杂度为 O(n^2),它最多能处理n大约为10^4的数据。当n接近10^5时就会超时。

'''
#自己的想法，显示超出时间限制
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)
        for i in range(len(set1)):
            if nums.count(nums[i]) > 1:
                return True
                break
            if i == len(set1):
                return False
				
				
#想到的另一种思路，因为字典的键是不能重复的所以利用字典
#188ms  击败19.38%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        if len(dic) < len(nums):
            return True
        else:
            return False
			
			
#我真的是傻了，set之后是去重的结果，为什么不直接比较和原数组的长度呢？
#136ms 95.58%
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set(nums)
        if len(set1) < len(nums):
            return True
        else:
            return False
			
#一行代码解决。。。
#144ms, 84.28% 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#利用哈希表
#144ms
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False