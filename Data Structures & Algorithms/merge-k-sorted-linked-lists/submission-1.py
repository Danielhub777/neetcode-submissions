# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        one = {}
        for i in lists:
            two = i
            while two != None:
                if two.val in one:
                    one[two.val]+=1
                else:
                    one[two.val]=1
                two = two.next
        three = sorted(one.items())
        print (three)

        Five = ListNode()
        Geek = Five
        if len(three) == 0:
            Five = None
        else: 
            for i in range(0, len(three)):
                for z in range(0, three[i][1]):
                    Geek.val = three[i][0]
                    if i + 1 == len(three) and z+1 == three[i][1]:
                        continue
                    else:
                        Six = ListNode()
                        Geek.next = Six
                        Geek = Geek.next
        return Five



