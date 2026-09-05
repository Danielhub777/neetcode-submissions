# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        three = head
        slow = three
        fast = three
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None 
        # while three is not None:
        #     count+=1
        #     three = three.next 
        # mid = int(count//2)
        # for i in range(mid-1):
        #     two = two.next
        # second = two.next
        # two.next = None 
        # print(second.val, head.val)
        prev = None 
        while second is not None:
            temp = second.next
            second.next = prev 
            prev = second 
            second = temp
        
        one = ListNode()
        mover = one 
        while prev is not None and head is not None:
           mover.next = head
           head = head.next
           mover = mover.next
           mover.next = prev
           prev = prev.next
           mover = mover.next
        mover.next = head or prev
        head = one.next

        # for i in range(mid-1):
        #     cur = head.next
        #     head.next = second
        #     second.next = cur
        #     head = head.next

            

