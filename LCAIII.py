# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Implement your solution here
        pass

# Helper function to find a node
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    return left if left else find_node(root.right, val)

# Test Cases
if __name__ == "__main__":
    # Creating a sample tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    # Instantiate solution
    sol = Solution()
    
    # Test cases
    print(sol.lowestCommonAncestor(root, root.left, root.right).val)  # Expected output: 3
    print(sol.lowestCommonAncestor(root, root.left, root.left.right.right).val)  # Expected output: 5
    print(sol.lowestCommonAncestor(root, find_node(root, 99), root.right.right))  # Expected output: None
