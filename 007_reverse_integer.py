'''
Reverse digits of an integer.

Example1: x = 123, return 321 Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note: The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

'''

class Solution():
    def reverse_integer(self, number):
        sign = number/abs(number)
        num = str(abs(number))
        while num[-1] == '0':
            num = num[:,-1]
        num = num[::-1]
        if num < str(2**31-1):
            return int(sign * int(num))
        else:
            return 0

# try to use more basic functions, avoid using str() function
class Solution2():
    def reverse_integer(self, number):
        sign = number/abs(number)
        num = abs(number)
        res = 0
        while num > 0:
            digit = num%10
            num = num//10
            if digit != 0:
                break
        res = res*10 + digit
        while num > 0:
            digit = num%10
            num = num//10
            res = res*10 + digit
            # in Java, res can overflow, need another condition statement, e.g., if (res - digit)*10 != num*10 + digit
            if res > 2**31 - 1:
                return 0
        return int(res*sign)
      
    
if __name__ == '__main__':
    a = Solution()
    print(a.reverse_integer(1000000003))
    b = Solution2()
    print(b.reverse_integer(1000000003))
   