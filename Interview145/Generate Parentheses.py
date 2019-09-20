"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Recursion with Backtracking (same as DFS)
The key to this problem is writing a recursive function that operates in a manner similar to how we would generate all valid pairs by hand.

At every step of the way, we choose to add either an open bracket or a close bracket. This can easily be implemented as part of the recursive call. The trick is to also implement the restraint, namely 'dont add a close bracket if there isnt already an open bracket'. AKA: only add if right > left. The restraint for adding open brackets is simple, add one if there are still open brackets to be added.

Following this logic allows us to only generate valid strings, and we are done generating a particular string when we dont have any more brackets left ot add.

Parameters:
(int) left: set to n, keep track of open brackets that need to be added
(int) right: set to n, keep track of close brackets that need to be add
(str) curr: set to "", used to store the current version of the string
(dict()) res: hold all valid strings, is returned by the function
"""
class Solution(object):
    def generateParenthesis(self, n):
        
		def paren(left, right, curr, res):
			# 'evaluate current string
			# if we are out of brackets to add, we must be at a valid string
			if left == 0 and right == 0:
				res.append(curr)
				return

			# recursive call: add either open or close
			# if adding open bracket is valid
			if left > 0:
				# add open bracket, decr count
				paren(left-1, right, curr + "(", res)

			# if adding close bracket is valid
			if right > left:
				# add close bracket, decr count
				paren(left, right-1, curr + ")", res)

			return res
		# end paren()

		res = paren(n, n, '', [])

		return res
