#给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#最简单直接的想法，最开始解答忽略了数组长度为1的情况
#用时：268 ms 17.34%
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        j=1
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                j += 1
                if j > len(nums)/2:
                    return nums[i]
                    break
            else:
                j = 1
				
#184 ms, 在所有 Python3 提交中击败了97.67%的用户
#同样是先排序，然后如果出现次数超过n/2,则在数组的中间位置一定为要找的数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2
        return nums[n]
		
#暴力解法，两层for循环嵌套，但是提交显示超出时间限制 时间复杂度O(n**2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            c = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    c += 1
            if c > n/2:
                return nums[i]
				
				
#利用哈希表，dic.get(i,0)即获得key为i的元素的value，如果值不在字典中返回default值
#48ms 击败 100% 方法对了简直是太快了
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        set1 = set(nums)
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        for i in set1:
            if dic.get(i) > len(nums) // 2:
                return i
				
#计数法，先set求集合，之后再使用list.count()函数计算出现次数
#40ms  击败100%
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set1 = set(nums)
        for i in set1:
            if nums.count(i) > len(nums) // 2:
                return i
				
#摩尔投票法 抵消的思想
#188ms
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        n = len(nums)
        target = nums[0]
        for i in range(1,n):
            if nums[i] == target:
                count += 1
            else:
                if count >= 1:
                    count -= 1
                else:
                    target = nums[i]
        return target
