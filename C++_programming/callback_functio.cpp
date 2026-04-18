#include<iostream>
using namespace std;
int sum(int a,int b)
{
    return a+b;
}
void gethello(int(*fptr)(int,int))
{
    cout<<"Hellow user"<<endl<<"the sum of two number is "<<fptr(6,7)<<endl;
}
void getgm(int(*fptr)(int,int))
{
    cout<<"Good morning user"<<endl<<"the sum of two number is "<<fptr(8,6)<<endl;
}
int main()
{
int (*ptr)(int ,int);
ptr=sum;
gethello(ptr);
getgm(ptr);
    return 0;
}