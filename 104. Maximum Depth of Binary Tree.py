class Solution(object):
    def maxDepth(self, root):
        def traverse(root,depth):
            if root == None: 
                return depth+0
            else: 
                return max(traverse(root.left,depth+1),traverse(root.right,depth+1))
        return traverse(root,0)
        