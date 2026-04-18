#include<iostream>
using namespace std;

class complex
{
    int a,b;
    friend complex sumcomplex(complex o1,complex o2);
    public:
    void setnumber(int n1,int n2)
    {
        a=n1;
        b=n2;
    }
    void prientnumber()
    {
        cout<<"You number is "<<a<<"+ "<<b<<"i"<<endl;
    }
};
complex sumcomplex(complex o1,complex o2)
{
    complex o3;
    o3.setnumber((o1.a+o2.a),(o1.b+o2.b));
    return o3;
}

int main()
{    complex c1,c2,sum;
    c1.setnumber(1,4);
    c1.prientnumber();
    c2.setnumber(7,5);
    c2.prientnumber();
    sum=sumcomplex(c1,c2);
    sum.prientnumber();
    return 0;
}