
'''
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#时间复杂度O(n),空间复杂度O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = set()
        cur = head
        while cur:
            if cur in a: 
                return True
            a.add(cur)
            cur = cur.next
        return False
		

#时间复杂度O(n),空间复杂度O(1)
#双指针，如果是环形，则两指针会相遇，如果不是环形，则fast或fast.next,fast.next.next为None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            if fast == None:
                return False
        return False

        


        
