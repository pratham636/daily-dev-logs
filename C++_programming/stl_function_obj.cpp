#include<iostream>
#include<functional>
#include<algorithm>
using namespace std;
int main()
{
 int arr[]={12,29,43,4,55,76}  ;
 sort(arr,arr+6,greater<int>());
for(int i=0;i<6;i++)
{
    cout<<arr[i]<<endl;
}
    return 0;
}