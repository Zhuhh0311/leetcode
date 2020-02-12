'''
外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
#给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#注意：整数序列中的每一项将表示为一个字符串
'''
#抄的
#哎
#执行用时 :40 ms, 在所有 Python3 提交中击败了65.41%的用户
class Solution:
    def countAndSay(self, n: int) -> str:
        prev_person = '1'
        for i in range(1,n):
            next_person, num, count = '', prev_person[0], 1
            for j in range(1, len(prev_person)):
                if prev_person[j] == num:
                    count += 1
                else:
                    next_person += str(count) + num
                    num = prev_person[j]
                    count = 1
            next_person += str(count) + num
            prev_person = next_person
        return prev_person
        