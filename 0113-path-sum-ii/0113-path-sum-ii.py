# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def func(node, cur, k):
            if not node:
                return

            cur.append(node.val)
            k += node.val

            if not node.left and not node.right and k == targetSum:
                res.append(cur.copy())

            func(node.left, cur, k)
            func(node.right, cur, k)

            cur.pop()

        func(root, [], 0)   
        return res