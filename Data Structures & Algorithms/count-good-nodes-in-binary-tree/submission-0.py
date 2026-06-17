# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            total_good_nodes = 0
            if not node:
                return total_good_nodes
            if node.val >= max_val:
                total_good_nodes += 1
            if node.left:
                left_count = dfs(node.left, max(max_val, node.val))
                total_good_nodes += left_count
            if node.right:
                right_count = dfs(node.right, max(max_val, node.val))
                total_good_nodes += right_count
                
            return total_good_nodes


        count = dfs(root, root.val)
        return count





        
        