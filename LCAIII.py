# Lowest Common Ancestor of a Binary Tree III
# 
# Given the root of a binary tree, and nodes p and q, return the lowest 
# common ancestor (LCA) of p and q.
# 
# Each node will have a pointer to its parent, and nodes p and q are
# guaranteed to be in the tree.
# 
# The LCA of two nodes p and q in a tree is the lowest node that has both 
# p and q as descendants, where we allow a node to be a descendant of itself.
# 
# Constraints:
# - The number of nodes in the tree is in the range [1, 10^4].
# - -10^9 <= Node.val <= 10^9
# - All Node.val are unique.
# - p and q are different nodes in the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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

    p = root.left          # Node 5
    q = root.left.right.right # Node 4
    solution = Solution()
    assert solution.lowestCommonAncestor(root, p, q) == p, "Test case 1 failed"

    p = root.left          # Node 5
    q = TreeNode(10)       # Node not in tree
    assert solution.lowestCommonAncestor(root, p, q) == None, "Test case 2 failed"

    print("All test cases pass for LCA III")

test()
