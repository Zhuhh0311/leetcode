#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

#最暴力的算法，自己想的，但是提交显示超出时间限制
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        a=-1
        while i < k:
            a = nums[len(nums)-1]
            for j in range(len(nums)-2, -1, -1):
                nums[j+1] = nums[j]
            nums[0] = a
            i += 1
			
#为了减少运行时间，考虑去掉第一种方法的for循环，转而使用python的内置函数insert pop
#执行用时 :152 ms, 在所有 Python3 提交中击败了25.00%的用户; 内存消耗 :14 MB, 在所有 Python3 提交中击败5.18%的用户
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        a = -1
        while i < k:
            a = nums[len(nums)-1]
            nums.insert(0, a)
            nums.pop()
            i += 1

#利用python的切片实现三次反转 64ms 在所有 Python3 提交中击败了94.61%的用户
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:n-k] = nums[:n-k][::-1]
        print(nums)
        nums[n-k:] = nums[n-k:][::-1]
        print(nums)
        nums[:] = nums[:][::-1]
#自己定义函数swap实现指定位置区间的元素反转 60ms 98.27%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        tmp = -1
        l=0
        r = n-1
        def swap(l,r):
            while l<r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l += 1
                r -= 1
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)
#更简洁的 60ms
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
