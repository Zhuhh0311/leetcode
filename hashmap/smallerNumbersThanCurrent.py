#1365. 有多少小于当前数字的数字
'''
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案。
示例 2：

输入：nums = [6,5,4,8]
输出：[2,1,0,3]
'''


#很想利用哈希表做，但是没想到咋做，只能先把暴力法写出来
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            h = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    h += 1
            res.append(h)
        return res
		
#自己摸索的第二种方法
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        num = sorted(nums)
        for i in range(len(nums)):
            res.append(num.index(nums[i]))
        return res
		
#下面这两种方法我都没有仔细研究		
		
#官方题解的  频次数组+前缀和
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt, vec = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(n):
            if nums[i]:
                vec[i] = cnt[nums[i] - 1]
        return vec
#利用哈希表
#时间复杂度：排序需要 O(nlogn) 的时间复杂度，遍历数组需要 O(n)的时间复杂度，所以总的时间复杂度为 O(nlogn+n)=O(nlogn)。
#空间复杂度：上文提及的 tmp数组需要 O(n)的空间，空间复杂度为 O(n)。

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vec = [0] * n
        tmp = sorted([(nums[i], i) for i in range(n)])
        
        pre = -1
        for i in range(n):
            if i != 0 and tmp[i][0] != tmp[i - 1][0]:
                pre = i - 1
            vec[tmp[i][1]] = pre + 1
        return vec

