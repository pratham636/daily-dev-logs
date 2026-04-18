#include<iostream>
using namespace std;
int sum(int n1,int n2)
{
    return n1+n2;
}
int main()
{
        int (*fun)(int,int);
        fun = &sum;
        int res1=fun(20,20);
        int res2=fun(20,20);
        cout<<res1<<endl<<res2;
    return 0;
}