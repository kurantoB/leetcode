class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        
        return countAndSayHelper(self.countAndSay(n - 1))
    
def countAndSayHelper(val):
    strVal = str(val)
    builder = ''
    currNum = strVal[0]
    currCount = 0
    for i in val:
        if i == currNum:
            currCount += 1
        else:
            builder += str(currCount) + str(currNum)
            currNum = i
            currCount = 1
    builder += str(currCount) + str(currNum)
    return builder