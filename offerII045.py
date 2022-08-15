# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        from collections import deque
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            res = []
            for _ in range(size):
                tmp = queue.popleft()
                res.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            result.append(res[:])
        return result[-1][0]