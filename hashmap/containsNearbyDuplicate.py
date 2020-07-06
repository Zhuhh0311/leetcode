#219. 存在重复元素 II
'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true
'''
#暴力方法解决问题，提交显示超出时间限制
#时间复杂度：O(nmin(k,n))，每次搜索都要花费 O(min(k,n)) 的时间
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j-i <= k:
                    return True
        return False

#刚开始就想利用hashmap来做，想把相同key的value值放在一个列表里，后来没有实现并且这样做之后还需要比较value列表里的值
#下面是若key已存在，则比较其value与i的差，若其差大于K，则更新value
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic.update({nums[i]:i})
            else:
                if i - dic.get(nums[i]) <= k:
                    return True
                else:#这个else去掉也 可以
                    dic[nums[i]] = i 
        return False

#参照题解来做的，设定hashmap的长度为k,遍历nums,当dic中存在当前元素则返回true否则添加元素，然后判断dic长度，长度超过k时删除dic中的第一个元素		
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic.update({nums[i]:i})
            if len(dic) > k:
                del dic[nums[i-k]]
        return False