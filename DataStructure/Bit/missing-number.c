// question number: https://leetcode.com/problems/missing-number/

int missingNumber(int* nums, int numsSize){
    int sol = 0;
    for (int i=0; i < numsSize; i++){
        sol ^= (i + 1) ^ nums[i];
    }
    return sol;
}
