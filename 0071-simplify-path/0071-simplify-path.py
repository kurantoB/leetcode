class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = Stack()
        
        elems = path.split('/')
        for elem in elems:
            if len(elem) == 0:
                continue
            if elem == '.':
                continue
            if elem == '..':
                if not stack.isEmpty():
                    stack.pop()
                continue
            newElem = StackElem(elem)
            stack.push(newElem)
        
        canonicalPath = ''
        
        while not stack.isEmpty():
            elem = stack.pop()
            canonicalPath = '/' + elem.data + canonicalPath

        if len(canonicalPath) == 0:
            canonicalPath = '/'
        
        return canonicalPath

class StackElem:
    next = None
    data = None
    
    def __init__(self, data):
        self.data = data
        
class Stack:
    head = None
    
    def push(self, elem):
        if self.head is not None:
            elem.next = self.head
        self.head = elem
    
    def pop(self):
        tmp = self.head
        self.head = self.head.next
        return tmp
    
    def isEmpty(self):
        return self.head == None