#1122. 数组的相对排序
'''
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

提示：
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
'''





#计数排序，把arr1 arr2中元素的值作为下标，出现一次其下标对应位置的值+1
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = [0 for _ in range(1001)]
        tmp = []
        for a in arr1:
            res[a] += 1
        for a in arr2:
            while res[a] > 0:
                tmp.append(a)
                res[a] -= 1

        for i in range(len(res)):
            while res[i] > 0:
                tmp.append(i)
                res[i] -= 1

        return tmp
        
#sort()函数是对列表正序排序，不会产生一个新列表。sorted()函数不会对原来列表产生影响，会产生一个有序的新列表
#对于字符串、字典这类不可修改类型没有sort方法
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for a in arr2:
            while a in arr1:
                res.append(a)
                arr1.remove(a)
        return res + sorted(arr1)
                
            



            

            



            
