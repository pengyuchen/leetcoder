class Solution(object):
    def isSameTree(self, p, q):
        def isSameTree_helper(p,q):
            if p == q == None:
                return True
            elif (p != None) and (q != None):
                return (p.val == q.val) and isSameTree_helper(p.left,q.left) and isSameTree_helper(p.right,q.right)
            else:
                return False
        return isSameTree_helper(p,q)
