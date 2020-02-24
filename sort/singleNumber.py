#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

#数学方法，这个太6了
#108ms  46.35%
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        return 2 * sum(set(nums)) - sum(nums)
        
#使用哈希表
#192ms   12.14%
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
        
        
#异或运算,这个方法也太66了吧
#104ms
class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        ans = 0
        for i in nums:
            ans = ans^i
        return ans
       
       