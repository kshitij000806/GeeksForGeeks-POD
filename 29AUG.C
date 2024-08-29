class Solution {
public:
    int countNodesinLoop(Node* head) {
        if (!head || !head->next) return 0;

        Node* slow = head;
        Node* fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) { 
                int loopSize = 1;
                Node* current = slow;
                while (current->next != slow) {
                    current = current->next;
                    loopSize++;
                }
                return loopSize;
            }
        }

        return 0; 
    }
};