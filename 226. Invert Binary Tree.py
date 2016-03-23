class Solution(object):
    def invertTree(self, root):
        def invert_helper(root):
            if root!= None:
                root.left, root.right = root.right, root.left
                invert_helper(root.left)
                invert_helper(root.right)
        invert_helper(root)
        return root
        