#剑指 Offer 59 - I. 滑动窗口的最大值
#给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

'''
示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums:
            return []
        for i in range(len(nums)-k+1):
            m = max(nums[i:i+k])
            res.append(m)
        return res
		
#题解
#自己的的方法实在是太慢了		
'''
算法流程：
初始化： 双端队列 deque ，结果列表 res，数组长度 n；
滑动窗口： 左边界范围 i∈[1−k,n+1−k] ，右边界范围j∈[0,n−1] ；
若 i > 0 且 队首元素 deque[0] == 被删除元素 nums[i - 1]：则队首元素出队；
删除 deque内所有 < nums[j] 的元素，以保持 deque递减；
将 nums[j] 添加至 deque尾部；
若已形成窗口（即 i≥0 ）：将窗口最大值（即队首元素 deque[0] ）添加至列表 res。
返回值： 返回结果列表 res。
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        for i in range(k):
            while deque and deque[-1] < nums[i]: deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]: deque.popleft()
            while deque and deque[-1] < nums[i]: deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res