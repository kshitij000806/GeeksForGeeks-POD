class Solution:
    def alternatingSplitList(self, head):
        if head is None:
            return None, None

        a_head = None
        b_head = None
        a_tail = None
        b_tail = None
        current = head

        while current is not None:
            if a_head is None:
                a_head = Node(current.data)
                a_tail = a_head
            else:
                a_tail.next = Node(current.data)
                a_tail = a_tail.next
            
            current = current.next
            if current is not None:
                if b_head is None:
                    b_head = Node(current.data)
                    b_tail = b_head
                else:
                    b_tail.next = Node(current.data)
                    b_tail = b_tail.next
                
                current = current.next
        
        return a_head, b_head
