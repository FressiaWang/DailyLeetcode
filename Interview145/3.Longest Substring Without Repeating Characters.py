"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
					    ^    ^
					    |     |
				      left  right		
current string:  a s[left:right+1]: a   left: 0   right: 0 res 1 seen {'a': 0}
current string:  ac s[left:right+1]: ac   left: 0   right: 1 res 2 seen {'a': 0, 'c': 1}
current string:  acb s[left:right+1]: acb   left: 0   right: 2 res 3 seen {'a': 0, 'c': 1, 'b': 2}
current string:  acbd s[left:right+1]: acbd   left: 0   right: 3 res 4 seen {'a': 0, 'c': 1, 'b': 2, 'd': 3}
current string:  acbdb s[left:right+1]: db   left: 3   right: 4 res 4 seen {'a': 0, 'c': 1, 'b': 4, 'd': 3}
current string:  acbdba s[left:right+1]: dba   left: 3   right: 5 res 4 seen {'a': 5, 'c': 1, 'b': 4, 'd': 3}
current string:  acbdbac s[left:right+1]: dbac   left: 3   right: 6 res 4 seen {'a': 5, 'c': 6, 'b': 4, 'd': 3}
current string:  acbdbacd s[left:right+1]: bacd   left: 4   right: 7 res 4 seen {'a': 5, 'c': 6, 'b': 4, 'd': 7}
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left,res = 0,0
        for right,v in enumerate(s):
            if v not in seen or seen[v]<left:
                res = max(res,right-left+1)
            else:
                left = seen[v] + 1
            seen[v] = right
        return res
def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = ''
        mx = 0
        for x in s:
            if x in seen:
                seen = seen[seen.index(x)+1:] + x
            else:
                seen += x
            mx = max(mx, len(seen))
        return mx
