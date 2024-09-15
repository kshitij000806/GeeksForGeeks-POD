class Solution:
    def __init__(self):
        self.prev = None
    def bToDLL(self, root):
        if root is None:
            return None
        head = self.bToDLL(root.left)
        if self.prev is None:
            head = root
        else:
            root.left = self.prev
            self.prev.right = root
        
        self.prev = root  
        self.bToDLL(root.right)
        
        return head
