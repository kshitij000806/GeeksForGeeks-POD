class Solution:
    def multiply_two_lists(self, first, second):
        num1 = 0
        num2 = 0
        MOD = 1000000007
        while first is not None:
            num1 = (num1 * 10 + first.data) % MOD
            first = first.next
        while second is not None:
            num2 = (num2 * 10 + second.data) % MOD
            second = second.next
        return (num1 * num2) % MOD
