#575. 分糖果
#给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
'''
示例 2 :
输入: candies = [1,1,2,3]
输出: 2
解析: 妹妹获得糖果[2,3],弟弟获得糖果[1,1]，妹妹有两种不同的糖果，弟弟只有一种。这样使得妹妹可以获得的糖果种类数最多。
'''

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        c = len(set(candies))
        l = len(candies) // 2
		#return min(l,c)可以一行解决问题。。。
        if c >= l:
            return l
        else:
            return c
