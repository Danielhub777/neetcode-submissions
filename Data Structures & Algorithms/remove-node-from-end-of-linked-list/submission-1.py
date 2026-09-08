# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        prev = None 
        count = 0
        tam = head
        while tam is not None:
            count+=1
            tam = tam.next
        print(count)
        loop = (count - n)
        print(loop)
        sam = head
        one = 0
        if head.next is None and n == 1:
            head = None
        elif head.next is None and n == 0:
            return head
        elif loop == 0:
            head = head.next
        else:
            while sam is not None:
                one+=1
                if one == loop:
                    print(one)
                    print(sam.val)
                    break
                sam = sam.next
        if sam.next is not None:
            sam.next = sam.next.next
        
        # if sam is not None or sam.next is not None:
        #     sam.next = sam.next.next
        # else:
        #     sam.next = None 
        # return head
    

    
        # while current is not None:
        #     temp = current.next
        #     current.next = prev
        #     prev = current
        #     current = temp
        # # print(prev.val)
        # sam = prev
        # # for i in range(1,n-1):
        # #     sam = sam.next
        # #     print (sam.val)
        # # sam.next = sam.next.next
        # # print (sam.val)
        # # if sam is not None:
        # #     if sam.next is not None:
        # #         sam.next = sam.next.next
        # while sam is not None:
        #     count+=1
        #     if count == n:
        #         if sam.next == None:
        #             sam = None
        #         else:
        #             sam.next = sam.next.next
        #             sam = None
        #     else:
        #         sam = sam.next
        # return prev 
        return head