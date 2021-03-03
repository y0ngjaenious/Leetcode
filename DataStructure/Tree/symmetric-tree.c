// question link: https://leetcode.com/problems/symmetric-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool helper(struct TreeNode *p1, struct TreeNode *p2);
bool isSymmetric(struct TreeNode* root){
    struct TreeNode *p1, *p2;
    p1 = root->left;
    p2 = root->right;
    if (p1 == NULL){
        if (p2 == NULL) return true;
        else return false;
    }
    if (p2 == NULL) return false;
    if (p1->val == p2->val){
        return helper(p1->left, p2->right) && helper(p1->right, p2->left);
    }
    else{
        return false;
    }
}

bool helper(struct TreeNode *p1, struct TreeNode *p2){
    if (p1 == NULL && p2 == NULL){
        return true;
    }
    if (p1 == NULL || p2 == NULL){
        return false;
    }
    if (p1->val == p2->val){
        return helper(p1->left, p2->right) && helper(p1->right, p2->left);
    }
    return false;
}
