"""
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, 
which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
"""
def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        i = 0
        while i < len(s):
            j = i+1
            value += v[s[i]]
            if j < len(s):
                if (s[i]=='I' and (s[j] in ['V','X'])) or (s[i]=='X' and (s[j] in           ['L','C'])) or (s[i]=='C' and (s[j] in ['D','M'])):
                    value += v[s[j]]-2*v[s[i]]
                    i += 2
                else: i += 1
            else: i += 1
        return value
  
def romanToInt(self, s: str) -> int:
	res, prev = 0, 0
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	for i in s[::-1]:          # rev the s
		if dict[i] >= prev:
			res += dict[i]     # sum the value iff previous value same or more
		else:
			res -= dict[i]     # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc 
		prev = dict[i]
	return res
