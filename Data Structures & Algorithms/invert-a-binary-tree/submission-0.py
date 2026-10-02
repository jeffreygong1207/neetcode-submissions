# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def flip(node):
            if node is None:
                return None
            else:
                temp = node.left
                node.left = node.right
                node.right = temp
                flip(node.left)
                flip(node.right)
            return node
        

        return flip(root)
        