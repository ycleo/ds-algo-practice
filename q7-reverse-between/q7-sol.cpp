// LeetCode 92.
// https://leetcode.com/problems/reverse-linked-list-ii/
/**
 * Definition for singly-linked list.
 */   
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
//   1  ->  [2 -> 3 -> 4 -> 5] -> 6
//  start  tail

//   1->5->4->3->2->6
//key point: 1->5   2->6

#include <iostream>
using namespace std;

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        
        int idx = 1;
        ListNode *curr = head;
        ListNode *start = head;
        
        while(idx < left) {
            start = curr;
            curr = curr->next;
            idx++;
        }
        
        ListNode *tail = curr;
        ListNode *next = nullptr;
        ListNode *ans = nullptr;
        
        while(idx <= right) {
            next = curr->next;
            curr->next = ans;
            ans = curr;
            curr = next;
            idx++;
        }
        
        start->next = ans;  // 1->5
        tail->next = curr;  // 2->6
        
        if(left > 1) {
            return head;
        } else {
            return ans;
        }  
        
    }
};

// time: O(n)
// space: O(1)