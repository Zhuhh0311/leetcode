#给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#你可以假设除了整数 0 之外，这个整数不会以零开头

#第一道在LeetCode独立多出来题，虽然试错了很多次~~~看了别人的代码才发现自己的代码这么烂，又臭又长

#1.执行用时 :24 ms, 在所有 Python3 提交中击败了99.74%的用户; 内存消耗 :12.8 MB, 在所有 Python3 提交中击败了99.82%的用户
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j=1
        if digits[len(digits) - 1] < 9:
           digits[len(digits) - 1] += 1
        else:
            for i in range(len(digits)-2, -1, -1):
                if digits[i] == 9:
                    j += 1
                else:
                    break
            if len(digits)-j > 0:
                digits[len(digits) - j-1] += 1
                while j > 0:
                    digits[len(digits) - j] = 0
                    j -= 1
            else:
                digits[len(digits) - j] = 1
                while j > 1:
                    digits[len(digits) - j + 1] = 0
                    j -= 1
                digits.append(0)

        return digits 
		
#2.执行用时 :32 ms;内存消耗 :12.6 MB
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits
