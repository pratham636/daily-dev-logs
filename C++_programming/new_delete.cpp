#include<iostream>
using namespace std;
int main()
{
    int a=8;
    int *p=&a;
    cout<<*p;
    int *pr =new int(4);
    cout<<*pr;
    int *arr = new int [3];
    arr[0]=10;
    arr[1]=20;
    arr[2]=30;
    for(int i=0;i<3;i++) cout<<endl<<arr[i];
    //delete operator
   // delete p;
    //cout<<endl<<*p;
    delete[] arr;
    for(int i=0;i<3;i++) cout<<endl<<arr[i];
return 0;
}
