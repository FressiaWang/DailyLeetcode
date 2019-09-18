"""
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a 
numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ''
        #remove left spaces
        str = str.lstrip(' ')
        
        # check empty string
        if (not str):
            return 0
        
        # check minus/plus signs
        if (str[0] == '-' or str[0] == '+'):
            num = str[0]
            str = str[1:]
            
        # check digits
        for ch in str:
            if (ch.isdigit()):
                num += ch
            else:
                break
                
        try: 
            value = int(num)
            #check overflow
            if (value.bit_length() >= 32):
                return (2**31-1) if value > 0 else -2**31
            return value
        except ValueError:
            return 0
def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """          
        if len(str) == 1 and str.isdigit(): return int(str)
        for i, s in enumerate(str):
            if s == ' ': continue
            if s in '+-' or s.isdigit(): break
            return 0
        if (not str) or ((i == len(str)-1) and not s.isdigit()): return 0
        for j in range(i+1,len(str)):
            if not str[j].isdigit(): break
        
        try:
            res = int(str[i:j+str[j].isdigit()])
            if (res.bit_length() >= 32):
                return (2**31-1) if res >0 else -2**31
            return res
        except ValueError:
            return 0
          
