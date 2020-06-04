#238. 除自身以外数组的乘积
#给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。


#执行出错，数组中含有0不能做分母，并且使用了除法
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [''] * len(nums)
        out = nums[0] * nums[1]
        for i in range(2, len(nums)):
            out *= nums[i]
        for i in range(len(nums)):
            output[i] = out // nums[i] 
        return output
		
		
#看了题解分析之后自己写的
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [''] * len(nums)
        R = [''] * len(nums)
        output = [''] * len(nums)
        L[0] = 1
        R[len(nums)-1] = 1
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            R[i] = R[i+1] * nums[i+1]
        for i in range(len(nums)):
            output[i] = L[i]* R[i]
        return output

#上一版本的简化版本
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, output = [0] * length, [0] * length, [0] * length
        L[0], R[length-1] = 1, 1
        for i in range(1, length):
            L[i] = L[i-1] * nums[i-1]
        for i in reversed(range(length-1)):
            R[i] = R[i+1] * nums[i+1]
        for i in range(length):
            output[i] = L[i] * R[i]
        return output

#上述方法的空间复杂度为O(n),下面方法的空间复杂度是O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i]*R
            R *= nums[i]
        return answer
#nums[i]左侧的值正常计算，右侧值的乘积动态改变
#这个方法绝了，这脑子是怎么想的哟，哎
      