#1356. 根据数字二进制下 1 的数目排序
'''
给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
请你返回排序后的数组。

示例 1：
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
'''
#想到转换为二进制后排序，但是不知道该如何对每一段1的个数相同的段排序。。。
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr1 = []
        for i in arr:
            arr1.append(bin(i))
        print(sorted(arr1))
		
'''
sorted(iterable[, key][, reverse])
从 iterable 中的项目返回新的排序列表。
有两个可选参数，必须指定为关键字参数。
key 指定一个参数的函数，用于从每个列表元素中提取比较键：key=str.lower。默认值为 None （直接比较元素）。
reverse 是一个布尔值。如果设置为 True，那么列表元素将按照每个比较反转进行排序。

sorted(iterable, key, reverse)
key参数，接收一个函数地址，用来设置排序条件，这里我们经常使用匿名函数。
iterable的每一个元素作为参数传入key函数，key函数的返回值就是排序依据，当返回值为一个元祖时，这个元祖中的多个元素即为多个排序条件，从前到后重要程度依次降低。
'''
#使用关键字key,先对二进制x中的个数排序，再对x大小排序
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'),x))
