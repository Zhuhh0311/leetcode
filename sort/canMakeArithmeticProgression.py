#1502. 判断能否形成等差数列
'''
给你一个数字数组 arr 。
如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

示例 1：
输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
'''
#好久没有看到题一下子就有思路了，直接想到的暴力法
'''
时间复杂度：O(nlogn)。排序的时间代价为 O(nlogn)，遍历序列的时间代价是 O(n)，故渐进时间复杂度为 O(nlogn+n)=O(nlogn)。
空间复杂度：O(logn)。快速排序中使用的栈空间期望是 O(logn)。
'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr_s = sorted(arr)#这里可以不使用sorted,直接arr.sort()这样能节省空间
        a = arr_s[1] - arr_s[0]
        for i in range(2,len(arr_s)):
            if arr_s[i] - arr_s[i-1] != a: return False
        return True
