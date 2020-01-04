#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

#1.超出时间限制
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = len(nums)
        for i in range (0, num):
            for j in range (i+1, num):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break   
					
					
#2.执行用时 :988 ms, 在所有 Python3 提交中击败了32.32%的用户;内存消耗 :13.7 MB, 在所有 Python3 提交中击败了70.93%的用户
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = len(nums)
        j = -1
        for i in range(num):
            temp = nums[i+1:]
            if (target - nums[i]) in temp:
                j = temp.index(target-nums[i]) + i+1
                return [i, j]
                break
'''				
哈希函数要做的事情是给一个任意大小的数据生成出一个固定长度的数据,一个可靠的哈希算法要满足三点:
 第一是安全，给定数据 M 容易算出哈希值 X ，而给定 X 不能算出 M ，或者说哈希算法应该是一个单向算法。
 第二是独一无二，两个不同的数据，要拥有不相同的哈希。
 第三是长度固定，给定一种哈希算法，不管输入是多大的数据，输出长度都是固定的。
'''
#3.执行用时 :52 ms, 在所有 Python3 提交中击败了96.71%的用户; 内存消耗 :14.9 MB, 在所有 Python3 提交中击败了5.的用户
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums): 
            j = hashmap.get(target - num)
            if j is not None and j != i:
                return [i, j] 
				
#4.执行用时 :84 ms, 在所有 Python3 提交中击败了51.53%的用户; 内存消耗 :14.3 MB, 在所有 Python3 提交中击败了34.12%的用户
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums): 
            if target-num in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i