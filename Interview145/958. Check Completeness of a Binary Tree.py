"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 
"""
def isCompleteTree(self, root):
        have_null = False
        Q = [root]
        while Q:
            node = Q.pop(0)
            if not node:
                have_null = True
                continue
            if have_null:
                return False
            Q.append(node.left)
            Q.append(node.right)
        return True
def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))
        return nodes[-1][1] == len(nodes)
