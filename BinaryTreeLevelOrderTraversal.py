# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:  # keep going until queue is empty, no more nodes
            level_size = len(queue)
            temp = []

            # Go for duration of level
            for i in range(level_size):
                # grab first node to check
                node = queue.popleft()
                temp.append(node.val)

                # Add children of each node popped from the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # When it goes back to the top it will no longer have the nodes from the last level 
            # and therefore when you check the length it is the length of the next level as its
            # all the children in the queue
            result.append(temp)
        
        return result