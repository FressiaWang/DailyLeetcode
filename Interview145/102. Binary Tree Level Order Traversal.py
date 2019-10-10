"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""
from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        result, queue = [], deque([root])
        
        while queue:
            level_len = len(queue) # 记录现在队列中的节点数量
            level_nodes = [] # 每层输出
            while level_len > 0: # 具体出队入队操作，保证本层所有节点的子节点都入队
                cur_node = queue.popleft()
                level_nodes.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                level_len -= 1
            result.append(level_nodes)
        
        return result
