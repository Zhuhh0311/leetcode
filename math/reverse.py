#给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#例如：123 --> 321, -123 --> -321, 120 --> 21
#执行用时 :52 ms, 在所有 Python3 提交中击败了12.31%的用户
class Solution:
    def reverse(self, x: int) -> int:
        y, res = abs(x), 0
        of = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > of:
                return 0
            y //= 10
        return res if x > 0 else -res
        
#先把int转化为字符串，进行字符串反转，再转回int，但是转回过程可能发生数据溢出
#40ms,提交时居然通过了
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[:0:-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0
        
       