#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
 void hi(){
 }
int main(){
    string input, nums = "";
    cin >> input;
    for(int i = 0; i < abs(input.length()); i++)
        if(input[i] != '+') nums += input[i];
    sort(nums.begin(), nums.end());
    for(int i = 0; i < abs(nums.length()); i++)
        if(i == abs(nums.length())-1) cout << nums[i];
        else cout << nums[i] << "+";
    return 0;
   
}
