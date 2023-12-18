class Solution(object):
    memo = {}
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """        
        if n in self.memo.keys():
            return self.memo[n]
        
        if n == 1:
            self.memo[1] = 1
            return 1
        
        val = self.numTrees(n - 1) * 2
        for i in range(1, n - 1):
            val += self.numTrees(i) * self.numTrees(n - 1 - i)
        
        self.memo[n] = val
        
        return val