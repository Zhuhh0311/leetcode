#1431. Kids With the Greatest Number of Candies
'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = max(candies)
        out = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= a:
                out.append(True)
            else:
                out.append(False)
        return out

#精简代码真的太重要了。。。
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies = max(candies)
        ret = [candy + extraCandies >= maxcandies for candy in candies]
        return ret