# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 分解成多个节点的路径和
    def rootsum(self, root, targetSum):
        if not root:
            return 0
        _sum = 0
        if root.val == targetSum:
            _sum += 1
        _sum += self.rootsum(root.left, targetSum - root.val)
        _sum += self.rootsum(root.right, targetSum - root.val)
        return _sum
    def pathSum(self, root, targetSum: int) -> int:
        if not root:
            return 0
        _sum = self.rootsum(root, targetSum)
        _sum += self.pathSum(root.left, targetSum)
        _sum += self.pathSum(root.right, targetSum)
        return _sum