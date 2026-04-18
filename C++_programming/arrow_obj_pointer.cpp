#include<iostream>
using namespace std;
class class1
{
int a,b;
public:
    void set(int y,int x)
    {
        a=y;
        b=x;
    }
    void get()
    {
        cout<<"a : "<<a<<endl<<"b : "<<b<<endl;
    }
};
int main()
{
    int size,i,a,b;
    cin>>size;
class1 *ptr=new class1 [size];
class1 *ptt=ptr;
for(i=0;i<size;i++)
{
    cin>>a>>b;
    ptr->set(a,b);
    ptr++;
}
for (i = 0; i <size; i++)
{
    ptt->get();
    ptt++;
}

    return 0;
}