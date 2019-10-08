"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
Let's look at a naive recursive algorithm:

Suppose you are given 1--n, and you want to generate all binary search trees. How do you do it? 
Suppose you put number i on the root, then simply

Generate all BST on the left branch by running the same algorithm
with 1--(i-1),
Generate all BST on the right branch by running the
same algorithm with (i+1)--n.
Take all combinations of left branch
and right branch, and that's it for i on the root.
Then you let i go from 1 to n. And that's it. If you want to write it in code, it's like
The only problem is, it's very slow, because for large n, you'll need to calculate countTrees(i) many many times, 
where i is a small number. Naturally, to speed it up, you just need to remember the result of countTrees(i), 
so that when you need it next time, you don't need to calculate.
Let's do that explicitly by having a list of n+1 numbers to store the calculation result!
"""
def countTrees(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
 
    Result = 0
    for i in xrange(n):
        LeftTrees = countTrees(i)
        RightTrees = countTrees(n - i - 1)
        Result += LeftTrees * RightTrees
    return Result
    
def countTrees(n, cache):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if cache[n] != -1: # -1 means we don't know countTrees(n) yet.
        return cache[n]

    Result = 0
    for i in xrange(n):
        LeftTrees = countTrees(i, cache)
        RightTrees = countTrees(n - i - 1, cache)
        Result += LeftTrees * RightTrees
    cache[n] = Result
    
 class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0]*(n+1) # include n=0
        res[0] = 1
        for i in range(n+1):
            for j in range(i):
                res[i] += res[j]*res[i-1-j]
        return res[n]
    return Result
