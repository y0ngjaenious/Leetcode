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
    if (root == NULL) return true;
    return helper(root->left, root->right);
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
