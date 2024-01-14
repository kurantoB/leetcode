class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        val = 0
        
        for i in range(len(s)):
            if is_subtraction(s, i):
                val -= value_of(s[i])
            else:
                val += value_of(s[i])
        
        return val

def value_of(letter):
    if letter == 'I':
        return 1
    if letter == 'V':
        return 5
    if letter == 'X':
        return 10
    if letter == 'L':
        return 50
    if letter == 'C':
        return 100
    if letter == 'D':
        return 500
    if letter == 'M':
        return 1000
    return 0

def is_subtraction(s, i):
    if i == len(s) - 1:
        return False
    return value_of(s[i]) < value_of(s[i + 1])