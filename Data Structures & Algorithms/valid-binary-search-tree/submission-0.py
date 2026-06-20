# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(curr, low, high):
            if not curr:
                return True
            
            if curr.val < high and curr.val > low:
                left = dfs(curr.left, low, curr.val)
                right = dfs(curr.right, curr.val, high)
            else:
                return False
        
            return left and right
                

       
        res = dfs(root, float('-inf'), float('inf'))
        return res