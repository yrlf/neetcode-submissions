# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(head):
            while head:
                print(head.val)
                head = head.next

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now slow is 2nd half list's head
        #print(slow.val)
        if n % 2 != 0:
            slow = slow.next

        p = head

        while p:
            if p.next == slow:
                break
            p = p.next
        
        #print(p.val)
        p.next = None
        # p is 1st link list's tail

        # reverse 2nd list

        pre = None
        cur = slow

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # new head of 2nd list:
        newHead2 = pre
        printList(newHead2)

        q = newHead2
        p = head
        while q:
            #print(p.val, q.val)
            p_nxt = p.next
            q_nxt = q.next

            p.next = q
            q.next = p_nxt
            p = p_nxt
            q = q_nxt


      
