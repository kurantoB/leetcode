class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = deque()
        
        elems = path.split('/')
        for elem in elems:
            if len(elem) == 0:
                continue
            if elem == '.':
                continue
            if elem == '..':
                if len(stack) is not 0:
                    stack.pop()
                continue
            stack.append(elem)
        
        canonicalPath = ''
        
        while len(stack) is not 0:
            elem = stack.pop()
            canonicalPath = '/' + elem + canonicalPath

        if len(canonicalPath) == 0:
            canonicalPath = '/'
        
        return canonicalPath