# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        stack = deque()
        stack.append(root)
        if not root:
            return []
        while stack:
            row = []
            n = len(stack)
            for _ in range(n):
                node = stack.popleft()
                row.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.append(row)
        return result
            


        