# question link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* n1 = nullptr;
        ListNode* n2 = nullptr;
        ListNode* helper = head;
        for(; helper != nullptr; helper = helper -> next){
            k -= 1;
            n2 = n2 == nullptr ? nullptr : n2->next;
            if(k == 0){
                n1 = helper;
                n2 = head;
            }
        }
        int tmp = n1->val;
        n1->val = n2->val;
        n2->val = tmp;
        return head;
    }
};
