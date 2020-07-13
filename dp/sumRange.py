#303. 区域和检索 - 数组不可变
'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
'''


#由于题干说到会多次调用sumrange函数，故先用dp[i]存储nums前i-1个值的和，用时访问即可
#时间复杂度：每次查询的时间 O(1)，O(N) 预计算时间。由于累积和被缓存，每个sumrange查询都可以用 O(1) 时间计算。
#空间复杂度：O(n).
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0]*(len(nums)+1)
        if not nums: return 
        self.dp[1] = nums[0]
        for i in range(1,len(nums)):
            self.dp[i+1] = sum(nums[:i+1])
        

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

#也可以用暴力法，在sumrange函数内从i到j加和，但是这样每次调用sumrange函数时间复杂度都为O(n),会超出时间限制。