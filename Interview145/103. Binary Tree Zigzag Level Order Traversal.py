"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res, level, count = [], [root], 0
        while level:
            res.append([node.val for node in level]) if count % 2 ==0 else res.append([node.val for node in level[::-1]])
            temp = []
            for node in level:
                temp += [node.left, node.right]
            level = [newnode for newnode in temp if newnode]
            count += 1
        return res
        
def zigzagLevelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res
