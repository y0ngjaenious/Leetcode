// question link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

#include <unordered_map>
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if (s.length() <= pow(2, k)) return false;
        std::unordered_map<string, int> map;
        for(int i=0; i <= s.length() - k; i++){
            map[s.substr(i, k)] = 1;
        }
        return map.size() == (int)pow(2, k);
    }
};
