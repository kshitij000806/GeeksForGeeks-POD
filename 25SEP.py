class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        second_half = slow
        if fast:
            second_half = slow.next  

        first_half = prev
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
