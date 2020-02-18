"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s,[],res)
        return res
    
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return
        for i in range(1,len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:],path+[s[:i]],res)

def partition(self, s):
    res = []
    self.dfs(s, [], res)
    return res

def dfs(self, s, path, res):
    if not s:
        res.append(path)
        return
    for i in range(1, len(s)+1):
        if self.isPal(s[:i]):
            self.dfs(s[i:], path+[s[:i]], res)
    
def isPal(self, s):
    return s == s[::-1]
