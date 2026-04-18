#include<iostream>
using namespace std;
int main()
{
    int a=890;
    float b=3442.543;
    void *p;
p=&a;
    cout<<*((int *)p)<<endl;
    p=&b;
    cout<<*((float *)p);

    return 0;
}