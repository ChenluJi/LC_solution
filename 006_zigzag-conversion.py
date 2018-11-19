'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P A H N A P L S I I G Y I R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
# other's
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        n = len(s)
        ans = []
        step = 2 * numRows - 2
        for i in range(numRows):
            one = i
            two = -i
            while one < n or two < n:
                if 0 <= two < n and one != two and i != numRows - 1:
                    ans.append(s[two])
                if one < n:
                    ans.append(s[one])
                one += step
                two += step
        return "".join(ans)

# mine
class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = ''
        step = 2*numRows - 2
        for i in range(numRows):
            if i == 0 or i == numRows-1:
                j = 0
                while i + j*step < len(s):
                    res += s[i+j*step]
                    j += 1
            else:
                j = 0
                while True:
                    if i + j*step < len(s):
                        res += s[i+j*step]
                    else:
                        break
                    if 2*numRows-2-i+j*step < len(s):
                        res += s[2*numRows-2-i+j*step]
                    else: 
                        break
                    j += 1
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.convert('0123456789', 6))
    b = Solution2()
    print(b.convert('0123456789', 6))