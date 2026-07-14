# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        ans=[]

        while queue:

            length=len(queue)
            temp_list=[]
            for _ in range(length):
                temp=queue.pop(0)

                temp_list.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

            ans.append(temp_list)

        return ans
            

        