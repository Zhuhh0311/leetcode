'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''
#参照了题解，二十多天没刷题，感觉手生了，希望接下来可以坚持下去
class Solution:
    def longestPalindrome(self, s):
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            #ans += v -（v&0）
            #在题解里看到这个位运算，但是这里报错，不知道错在哪里
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans