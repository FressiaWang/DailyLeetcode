"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().
"""
#first version 
def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle : return 0
        if len(haystack) > len(needle):
            for i in range(len(haystack)-len(needle)+1): #need + 1
                if haystack[i:i+len(needle)] == needle:
                    return i
            return -1
        else:
            return 0 if haystack == needle else -1

#second version
def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or haystack == needle: 
            return 0
        if len(haystack) > len(needle):
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
