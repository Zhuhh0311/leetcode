#1295. 统计位数为偶数的数字
#给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。

#强制转换数字为字符串，计算字符串长度
#做做简单的题涨自信。。。
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            n = str(nums[i])
            if len(n) % 2 == 0:
                num += 1
        return num

		

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            if int(math.log10(nums[i])+1) % 2 == 0:
                num += 1
        return num