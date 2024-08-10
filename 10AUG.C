class Solution {
  public:
    Node* rotate(Node* head, int k) 
    {
        Node * start = NULL, *end = head, *p = head;
        int i = 1;
        while(end->next != NULL)
        {
            if(k == i){start = end;}
            end = end->next;
            i++;
        }
        if(start == NULL){return head;}
        head = start->next;
        start->next = NULL;
        end->next = p;
        return head;
    }
};
