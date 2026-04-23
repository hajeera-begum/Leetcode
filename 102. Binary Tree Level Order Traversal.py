'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use a queue to perform BFS (level-by-level traversal)
        q = collections.deque()
        
        # Final result storing values level-wise
        result = []
        
        # Start with root node
        q.append(root)

        # Continue until all levels are processed
        while q:
            level = []
            
            # Process all nodes currently in the queue (one full level)
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    # Add current node value to this level
                    level.append(node.val)
                    
                    # Add children to queue for next level
                    q.append(node.left)
                    q.append(node.right)
            
            # Only add non-empty levels (avoids adding levels with None nodes)
            if level:
                result.append(level)
        
        return result
