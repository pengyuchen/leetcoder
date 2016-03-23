class Solution(object):
    def reverseList(self, head):
        last = None
        while(head != None):
            next = head.next
            head.next = last 
            last = head
            head = next
        return last