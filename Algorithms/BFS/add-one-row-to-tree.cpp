// question link: https://leetcode.com/problems/add-one-row-to-tree/

#include <queue>
#include <unordered_map>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if (d == 1){
            TreeNode* new_root = new TreeNode(v);
            new_root->left = root;
            return new_root;
        }
        std::unordered_map<TreeNode*, int> map;
        std::queue<TreeNode*> q;
        map[root] = 1;
        q.push(root);
        while (!q.empty()){
            TreeNode*& e = q.front();
            
            if(map[e] == d - 1){
                TreeNode* l = new TreeNode(v);
                TreeNode* r = new TreeNode(v);
                if (e->left != NULL){
                    l->left = e->left;
                }
                if (e->right != NULL){
                    r->right = e->right;    
                }
                e->left = l;
                e->right = r;
            }
            else{
                if (e->left != NULL){
                    q.push(e->left);
                    map[e->left] = map[e] + 1;
                    std::cout << map[e->left] << std::endl;
                }
                if (e->right != NULL){
                    q.push(e->right);
                    map[e->right] = map[e] + 1;
                    std::cout << map[e->right] << std::endl;
                }
            }
            map.erase(e);
            q.pop();
        }
        
        return root;
    }
};
