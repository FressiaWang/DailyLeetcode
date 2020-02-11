"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    i, j = i+1, j-1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True
        
def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [i for i in s.lower() if i.isalnum()]
    	return s == s[::-1]
