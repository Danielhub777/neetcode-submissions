# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # one = head
        # while one.next != None:
        #     one = one.next
        # two = head
        # while two.next != None:
        # temp = head
        # one = head.next
        # while temp.next.next != None:
        #     temp.next.next = temp
        #     temp = one
        #     one = one.next
        # temp.next.next = temp
        # one = one.next
        # return one 
        current = head
        prev = None
        while current is not None:
            next_Node = current.next
            current.next = prev
            prev = current 
            current = next_Node
        return prev
        

        
        