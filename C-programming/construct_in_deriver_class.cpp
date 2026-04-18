#include<iostream>
using namespace std;
class a
{
    int base1;
    public:
    a()
    {}
    a(int x)
    {
        cout<<"b1 call"<<endl;
        base1=x;
    }
    void printb1()
    {
        cout<<base1<<endl;
    }
};
class b
{
    int base2;
    public:
     b()
    {}
    b(int y)
    {
        base2=y;
        cout<<"b2 call"<<endl;
    }
    void prinrb2()
    {
        cout<<base2<<endl;
    }
};
class c : public a,public b
{
    int derive1,deriver2;
    public:
    c()
    {}
    c(int e,int f,int g,int h):b(f),a(e)
    {
        cout<<"C call"<<endl;
        derive1=g;
        deriver2=h;
    }
    void printc(){
        cout<<"g and h ="<<derive1<<" "<<deriver2<<endl;
    }
};
int main()
{
     int s,y,z,d;
    cin>>s>>y>>z>>d;
   // a ax;
    //b bx;
    c cx(s,y,z,d);
    cx.printb1();
    cx.prinrb2();
    cx.printc();
    return 0;
}