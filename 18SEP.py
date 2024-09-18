class Solution:
    def ispar(self, x):
        stack = []
        
        for c in x:
            if c in "({[":
                stack.append(c)
            elif c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False

        return not stack
