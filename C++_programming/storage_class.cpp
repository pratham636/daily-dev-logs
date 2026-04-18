#include<iostream>
using namespace std;
int fun(int a,int b)
{
    auto int sum=a+b;
    return sum;
}
int main()
{
int sum;
fun(4,5);
cout<<sum;
    return 0;
}