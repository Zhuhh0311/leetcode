#922. 按奇偶排序数组 II
'''
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
'''
#自己想的暴力法，使用了额外的内存，面试时可能会要求写空间复杂度为O(1)的方法
#时间O(n),空间O(n)
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i,j = 0, 1
        res = [0 for _ in range(len(A))]
        for a in A:
            if a % 2 == 0:
                res[i] = a 
                i += 2
            else:
                res[j] = a
                j += 2
        return res 
		
#双指针，只需考虑偶数下标，如果偶数下标的元素均为偶数，则奇数元素也都在正确位置
#若偶数下标的元素为奇数，当奇数下标的元素为奇数时，奇数下标指向下一个奇数，直到碰到偶数，此时交换奇偶坐标元素，继续进行遍历的下一结果
#时间O(n),空间O(n)
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 != 0:
                while A[j] % 2 != 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
