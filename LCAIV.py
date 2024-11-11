# Lowest Common Ancestor of a Binary Tree IV
# 
# Given the root of a binary tree and a list of nodes, return the lowest 
# common ancestor (LCA) of all the nodes in the list.
# 
# The LCA of multiple nodes in a tree is the lowest node that has all nodes 
# as descendants, where we allow a node to be a descendant of itself.
# 
# Constraints:
# - The number of nodes in the tree is in the range [1, 10^4].
# - The number of nodes in the list is in the range [1, 10^4].
# - All Node.val are unique.
# - All nodes in the list are distinct.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Fill in your solution here
        pass

# Test cases
def test():
    # Tree setup
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    nodes = [root.left, root.left.right.right, root.right]
    solution = Solution()
    assert solution.lowestCommonAncestor(root, nodes) == root, "Test case 1 failed"

    nodes = [root.left.left, root.left.right.left, root.left.right.right]
    assert solution.lowestCommonAncestor(root, nodes) == root.left, "Test case 2 failed"

    print("All test cases pass for LCA IV")

test()
