# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        from collections import deque
        que = deque([root])
        res = []
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                if k - cur.val in res:
                    return True
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return False

