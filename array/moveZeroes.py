#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#自己想到的方法，之前一度陷入死循环，以后做题时要注意循环开始和结束的条件等
#84ms
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = nums.count(0)
        i = 0
        while i < len(nums)-m:
            if nums[i] == 0:
                nums.insert(len(nums), 0)
				#nums.append(0)也可以
                nums.pop(i)
            else:
                i += 1
#将不为0的元素挪到数组前面，记录不为0的元素个数index，将nums 在index下标后的值附为0
#56ms 86.06%
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range (len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0