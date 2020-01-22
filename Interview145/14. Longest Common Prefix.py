"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
#Approach 1: Horizontal scanning
def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] if strs else ''
        for s in strs[1:]:
            while (not s.startswith(prefix) and prefix):
                prefix = prefix[:-1]
        return prefix

def longestCommonPrefix(self, strs):
        prefix = strs[0] if strs else ''
        while True:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]
            
#Approach 2: Vertical scanning
def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        l = len(strs)
        for s in zip(*strs):
            if s == tuple(s[0]*l):
                prefix += s[0]
            else:
                break
        return prefix
 
def longestCommonPrefix(self, strs: List[str]) -> str:
        len_ = 0
        for i in zip(*strs):
            if len(set(i)) == 1:
                len_ += 1
            else: 
                break
        return strs[0][:len_] if len_ > 0 else ''
#
def longestCommonPrefix(self, S: List[str]) -> str:
        if not S: return ''
        m, M, i = min(S), max(S), 0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: break
        else: i += 1
        return m[:i]
