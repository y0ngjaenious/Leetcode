// question link: https://leetcode.com/problems/integer-to-roman/

#include<unordered_map>
#include<string>

class Solution {
public:
    string intToRoman(int num) {
        std::string output;
        std::unordered_map<int, std::string> map;
        map[1000] =  "M";
        map[900] = "CM";
        map[500] = "D";
        map[400] = "CD";
        map[100] = "C";
        map[90] = "XC";
        map[50] = "L";
        map[40] = "XL";
        map[10] = "X";
        map[9] = "IX";
        map[5] = "V";
        map[4] = "IV";
        map[1] = "I";
        
        int arr[13] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        for(auto& i: arr){
            int quo;
            quo = num / i;
            for(char& c: map[i]) output.append(quo, c);
            num = num % i;
        }
        return output;
    }
};
