'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
'''
#找到所有数组中消失的数字  热题100
#自己的想法，不满足题意，笨方法
#668 ms, 在所有 Python3 提交中击败了9.48%的用户

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = len(nums)
        l = set(nums)
        b = []
        for i in range(1,a+1):
            if i not in l:
                b.append(i)
        return b