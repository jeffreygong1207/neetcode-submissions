# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def search(node, current):
            nonlocal longest
            if node == None:
                return
            if node.left:
                search(node.left, current+1)
            if node.right:
                search(node.right, current+1)
            longest = max(longest, current)
            return

        search(root, 1)
        return longest
        