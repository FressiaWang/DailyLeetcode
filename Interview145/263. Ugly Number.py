"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
"""
def isUgly(self, num):
        """
        :type num: int
        :rtype: bool

 a == b < c actually means a == b and b < c in python! Amazing!
        """
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1
        
