# Visualization of the Tree:
#         3
#        / \
#       5   1
#      /|   |\
#     6 2   0 8
#      / \
#     7   4


# Definition for a binary tree node with a parent pointer.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, p: TreeNode, q: TreeNode) -> TreeNode:
        # Implement your solution here
        pathP = []
        pathQ = []
        
        while p or q:
            if p:
                if p in pathQ:
                    return p
                pathP.append(p)
                p = p.parent
            
            if q:
                if q in pathP:
                    return q
                pathQ.append(q)
                q = q.parent
                
        return None
        
    
    
    
    
    

# Helper function to set parent pointers
def set_parents(root):
    if root:
        if root.left:
            root.left.parent = root
            set_parents(root.left)
        if root.right:
            root.right.parent = root
            set_parents(root.right)

# Test Cases
if __name__ == "__main__":
    # Creating a sample tree with parent pointers
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    # Set parent pointers
    set_parents(root)
    
    # Instantiate solution
    sol = Solution()
    
    # Test cases
    print(sol.lowestCommonAncestor(root.left, root.right).val)  # Expected output: 3
    print(sol.lowestCommonAncestor(root.left, root.left.right.right).val)  # Expected output: 5
    print(sol.lowestCommonAncestor(root.right.left, root.right.right).val)  # Expected output: 1
