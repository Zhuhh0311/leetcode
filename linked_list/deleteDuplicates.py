#83. 删除排序链表中的重复元素
'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        pre = head
        cur = head.next
        while pre and cur:
            if pre.val == cur.val:  
                cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return head
#其实只需要这种写法就可以了。。。	
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:  
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head