# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self,head):
        prev=None
        while head:
            front=head.next
            head.next=prev
            prev=head
            head=front
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow=self.reverseLL(slow)
        cur=head
        while slow:
            if cur.val!=slow.val:
                return False
            cur=cur.next
            slow=slow.next
        return True
        