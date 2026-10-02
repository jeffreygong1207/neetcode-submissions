# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        #check contained in right or left

        # if one in either side then must be ancestor
        if p.val >= root.val and q.val <= root.val:
            return root
        elif p.val <= root.val and q.val >= root.val:
            return root
        
        #otherwise we need to check either side
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return self.lowestCommonAncestor(root.left, p,q)
        
        