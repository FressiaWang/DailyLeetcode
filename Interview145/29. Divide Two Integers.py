"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 
when the division result overflows.
"""
def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))
        
 def divide(self, dividend: int, divisor: int) -> int:
		is_negative = (dividend < 0) != (divisor < 0)
		divisor, dividend = abs(divisor), abs(dividend)

		quotient = 0
		the_sum = divisor

		while the_sum <= dividend:
			current_quotient = 1
			while (the_sum + the_sum) <= dividend:
				the_sum += the_sum
				current_quotient += current_quotient
			dividend -= the_sum
			the_sum = divisor
			quotient += current_quotient

		return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

"""
How it works
For example, we divide(5000, 14):

After the first inner loop: the_sum = 3584 which is 14 multiplied 256 times.
We can't multiply any more — because after 256 is coming 256 + 256 = 512 and 14 * 512 = 7168 
which is larger than our dividend, so we exit the inner loop,
Reducing dividend: dividend = 5000 - 3584 = 1416
And moving to another cycle of outer loop
After the second inner loop: the_sum = 896 which is 14 multiplied 64 times.
Third: the_sum = 448 which is 14 multiplied 32 times.
And so on
Finally we have: quotient = 256 + 64 + 32 + 4 + 1 = 357
"""
