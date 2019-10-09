"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
Approach 1: Recursive
Complexity Analysis

Time complexity : O(n)O(n). Because we traverse the entire input tree once, the total run time is O(n)O(n),
where nn is the total number of nodes in the tree.

Space complexity : The number of recursive calls is bound by the height of the tree. 
In the worst case, the tree is linear and the height is in O(n)O(n). 
Therefore, space complexity due to recursive calls on the stack is O(n)O(n) in the worst case.
Approach 2: Iterative
Instead of recursion, we can also use iteration with the aid of a queue. Each two consecutive nodes in the queue should be equal,
and their subtrees a mirror of each other. Initially, the queue contains root and root. Then the algorithm works similarly to BFS, 
with some key differences. Each time, two nodes are extracted and their values compared. Then, the right and left children of 
the two nodes are inserted in the queue in opposite order. The algorithm is done when either the queue is empty, or we detect that 
the tree is not symmetric (i.e. we pull out two consecutive nodes from the queue that are unequal).
"""
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def Mirror(L,R):
            if L and R:
                return (L.val == R.val) and Mirror(L.left,R.right) and                Mirror(L.right,R.left)
            else:
                return L == R
        return Mirror(root,root)
        
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [root.left,root.right] if root else []
        while nodes:
            L, R = nodes.pop(),nodes.pop()
            if L == R:continue
            if (not L or not R) or (L.val != R.val): 
                return False
            nodes.extend([L.left,R.right,L.right,R.left])
        return True
