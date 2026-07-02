# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1=headA
        p2=headB
        m=0
        n=0
        while p1:
            m+=1
            p1=p1.next
        while p2:
            n+=1
            p2=p2.next
        if m>n:
            for _ in range(m-n):
                headA=headA.next
        else:
            for _ in range(n-m):
                headB=headB.next
        # print(headA)
        # print(headB)
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None
        