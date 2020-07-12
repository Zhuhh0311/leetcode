#234. 回文链表
#这道题递归的解法还没有仔细看！！！
'''
请判断一个链表是否为回文链表。
 
示例 1:
输入: 1->2
输出: false
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#时间复杂度O(n),空间复杂度O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        print(arr)
		#return arr == arr[::-1]
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr)-1-i]:
                return False
        return True

#想要实现时间复杂度为O(n),空间复杂度为O(1)		
'''
我们可以分为以下几个步骤：

找到前半部分链表的尾节点。
反转后半部分链表。
判断是否为回文。
恢复链表。
返回结果。
'''		
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next
        first_half_end.next = self.reverse_list(second_half_start)
        return result
 

        def end_of_first_half(self, head):
            fast = head
            slow = head
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow
        def reverse_list(self, head):
            previous = None
            current = head
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous
