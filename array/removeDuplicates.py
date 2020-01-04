#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

#1.从后往前遍历，遇到相同的则删除相同中后面的一项
#执行用时 :156 ms, 在所有 Python3 提交中击败了17.65%的用户; 内存消耗：14.4 MB, 在所有 Python3 提交中击败了99.24%的用户。
#List pop 函数：pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = len(nums)
        for i in range(num-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)

		
#2.使用双指针的思路，i是慢指针，j是快指针
#执行用时 :92 ms, 在所有 Python3 提交中击败了93.03%的用户； 内存消耗 :14.5 MB, 在所有 Python3 提交中击败了98.23%的用户
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
        return i+1