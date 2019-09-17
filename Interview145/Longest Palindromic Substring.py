"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
palindrome function finds the longest palindrome in string s expand at
(1) the center m
or
(2) the center between m and m+1.
Time complexity: O(n^2)
where n is the length of the input string.
The algorithm needs to iterate throught the string call palindrome function 2n times. Each time call palindrome function it may go through the whole string, which costs n. So the total time complexity is O(2n*n) = O(n)
Space complexity: O(n)
The algorithm needs to maintain two string: sub, and longest, which costs O(n) where n is the length of the input string.
The algorithm needs to maintain three varialbes: m, l, r.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        longest = ""
        for i in range(len(s)):
            sub = self.palindrome(s,i,i)
            longest = sub if len(sub) > len(longest) else longest
            sub = self.palindrome(s,i,i+1)
            longest = sub if len(sub) > len(longest) else longest
        return longest
    def palindrome(self,s,l,r):
        while l >=0 and r < len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
