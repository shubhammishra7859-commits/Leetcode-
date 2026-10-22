class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        # Handle the special overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine if the result is negative
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        while a >= b:
            temp_divisor, multiple = b, 1
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            a -= temp_divisor
            quotient += multiple
            
        return -quotient if negative else quotient