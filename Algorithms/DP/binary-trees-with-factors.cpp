// question link: https://leetcode.com/problems/binary-trees-with-factors/

#include <unordered_map>
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        std::unordered_map<int, long> map;
        long mod = pow(10, 9) + 7;
        long ans = 0;
        double lim = 0;
        for(auto& i: arr){
            long ways = 1;
            lim = std::sqrt(i);
            for(int j = 0, a = arr[0]; a <= lim; a = arr[++j]){
                if(i % a != 0) continue;
                int b = i / a;
                if(map.find(b) != map.end())
                    ways += (map[a] * map[b] * (a == b ? 1 : 2));
            }
            map[i] = ways;
            ans = (ans + ways) % (mod);
        }
        return int(ans);
    }
};
