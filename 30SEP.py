class Solution:
    def pushLeft(self, root, stack):
        while root:
            stack.append(root)
            root = root.left
    
    def merge(self, root1, root2):
        result = []
        s1, s2 = [], []
        self.pushLeft(root1, s1)
        self.pushLeft(root2, s2)
        
        while s1 or s2:
            if not s2 or (s1 and s1[-1].data <= s2[-1].data):
                node = s1.pop()
                result.append(node.data)
                self.pushLeft(node.right, s1)
            else:
                node = s2.pop()
                result.append(node.data)
                self.pushLeft(node.right, s2)
        
        return result
