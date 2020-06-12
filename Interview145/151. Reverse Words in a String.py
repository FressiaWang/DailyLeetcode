"""
Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
"""
def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])
        
def reverseWords(self, s):
        # First reverse entire string, then iterate over reversed string
        # and again reverse order of characters within a word. Append each word to words.
        word = ""
        words = ""
        s = s[::-1]
        for j, i in enumerate(s):
            # character is not space, a current word exists, 
            # and previous character is space, e.g. i=b in " a b":
            if i != " " and word != "" and s[j-1] == " ":
                # add current word to words and append " " to later add this i
                words += (word + " ")
                word = i
            # character is not space, but it's either first character in string
            # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
            elif i != " ":
                word = i + word
            else:
                continue

        words += word
        
        return(words)
