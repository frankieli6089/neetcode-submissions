# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checkSubtreeEqual(curr, subcurr):
            if not curr and not subcurr:
                return True
            
            if not curr or not subcurr:
                return False

            if curr.val == subcurr.val:
                left = checkSubtreeEqual(curr.left, subcurr.left)
                right = checkSubtreeEqual(curr.right, subcurr.right)
            else:
                return False
            
            return left and right
        

        if checkSubtreeEqual(root, subRoot):
            return True
        if not subRoot:
            return True
        if not root:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return (left or right)
        


      