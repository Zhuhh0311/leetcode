#475. 供暖器 
'''
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:
给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
'''


#没理解题意，我以为房屋的位置是从1开始的连续的整数
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        b = heaters[0] - houses[0]
        a = 0
        for i in range(1, len(heaters)):
            a = max(heaters[i] - heaters[i-1], a)
        c = max(houses[-1] - heaters[-1], a // 2,b)
        return c
		
from typing import List
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        """存放每个房屋与加热器的最短距离"""
        res = []
        heaters.sort()#原来加热器也可以不按顺序放在数组里。。。
        for c in houses:#而且房屋也可以不按顺序。。。但是此方法不需要对房屋排序
            """二分查找"""
            left = 0
            right = len(heaters) - 1
            while left < right:
                mid = (left + right) >> 1
                if heaters[mid] < c:
                    left = mid + 1
                else:
                    right = mid
            """得出的 left 所指的加热器并不一定是离房屋 c 最近的一个，需要判断以下情况"""
            if heaters[left] == c:
                """若找到的值等于 c ，则说明 c 房屋处放有一个加热器，c 房屋到加热器的最短距离为 0"""
                res.append(0)

            elif heaters[left] < c:
                """若该加热器的坐标值小于 c ，说明该加热器的坐标与 c 之间没有别的加热器"""
                res.append(c - heaters[left])

            elif left == 0:
                """
                若left == 0 即二分查找的结果指向第一个加热器的坐标,说明 heaters[left] 坐标的房屋之前的位置
                未放置加热器,直接相减就是到房屋 c 最近加热器的距离
                """
                res.append(heaters[left] - c)
                
            else:
                """
                若left不等于 0 ，说明 c 介于left和left-1之间，房屋到加热器的最短距离就是left和left - 1处
                加热器与 c 差值的最小值.
                """
                res.append(min(heaters[left] - c, c - heaters[left - 1]))
                
        return max(res)
