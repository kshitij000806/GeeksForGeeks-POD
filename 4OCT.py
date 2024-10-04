class Solution:
    def reverse(self, head):
        if head is None or head.next == head:
            return head

        prev = head
        current = head.next
        nextNode = None

        while current != head:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        head.next = prev  
        return prev  

    def deleteNode(self, head, key):
        if head is None:
            return head

        current = head
        prev = None

        while True:
            if current.data == key:
                if current == head and current.next == head:
                    return None  

                if current == head:
                    tail = head
                    while tail.next != head:
                        tail = tail.next
                    head = current.next  
                    tail.next = head  
                else:
                    prev.next = current.next  
                return head

            prev = current
            current = current.next

            if current == head:
                break  

        return head  
