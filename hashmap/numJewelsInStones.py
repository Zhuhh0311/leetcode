#771. 宝石与石头
'''
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:
输入: J = "aA", S = "aAAbbbb"
输出: 3
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = []
        hashmap = {i:1 for i in J}
        for s in S:
            res.append(hashmap.get(s, 0))
        return sum(res)

		

#python之一行解决
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(i) for i in J)

#暴力法
#时间复杂度：O(J.length * S.length));空间复杂度O(1)
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)

#hashmap
#时间复杂度：O(J.length + S.length))这部分来自于创建 J，O(S.length)这部分来自于搜索 S; 空间复杂度：O(J.length)
		
class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
		#print(Jset)  {'A', 'a'}
        return sum(s in Jset for s in S)