"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""
def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, h = 0, x
        while l <= h: #判断条件包含=是为了考虑0这种情况
            mid = (l + h) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                h = mid 
            else:
                l = mid + 1 # + 1 是为了解决x=1 只有一个元素时避免进入无限循环
def mySqrt(self, x):
        if x == x*x: return x
        l, h = 0, x
        while l < h:
            mid = (l + h) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                h = mid 
            else:
                l = mid + 1
def mySqrt(self, x):
        l, h = 0, x
        while l < h:
            mid = (l + h) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                h = mid 
            else:
                l = mid + 1
        return l
