#include<iostream>
using namespace std;
template<class t1=int,class t2=float,class t3=char>
class Harry
{
    public:
    t1 a;
    t2 b;
    t3 c;
    Harry(t1 x,t2 y,t3 z)
    {
        a= x;
        b=y;
        c=z;
    }
    void display()
    {
        cout<<endl<<"a: "<<a<<endl<<"b: "<<b<<endl<<"c: "<<c;
    }
};

int main()
{
Harry<> h(4,5.709,'i');
h.display();
Harry<float,char ,char>j(6.789,'g','o');
j.display();

    return 0;
}