class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ans = l3 = ListNode(0)
        while(l1 != None or l2 != None or carry != 0):
            _sum = (( 0 if l1 == None else l1.val) + ( 0 if l2 == None else l2.val) + carry)
            carry, l3.val = _sum / 10, _sum % 10
            l1 = (None if l1 == None else l1.next)
            l2 = (None if l2 == None else l2.next)
            l3.next = ListNode(0) if (l1 != None or l2 != None or carry != 0) else None
            l3 = l3.next if l3 else None
        return ans
