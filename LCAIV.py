# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: list[TreeNode]) -> TreeNode:
        # Implement your solution here
        pass

# Helper function to find nodes based on values
def find_nodes(root, values):
    result = []
    def dfs(node):
        if node:
            if node.val in values:
                result.append(node)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result

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
    nodes = find_nodes(root, [5, 1])
    print(sol.lowestCommonAncestor(root, nodes).val)  # Expected output: 3
    
    nodes = find_nodes(root, [5, 4, 7])
    print(sol.lowestCommonAncestor(root, nodes).val)  # Expected output: 5
    
    nodes = find_nodes(root, [6, 7, 4])
    print(sol.lowestCommonAncestor(root, nodes).val)  # Expected output: 5
