#include<iostream>
using namespace std;
int main()
{
    int a=4900;
    int *ptr=NULL;
    //int *ptr=&a;
    if(ptr!=NULL)   cout<<*ptr<<endl;
   else  cout<<"NULL pointer";
    return 0;
}