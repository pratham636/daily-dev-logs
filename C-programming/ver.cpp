#include<iostream>
using namespace std;
class a
{
    public:
    void geating()
    {
        cout<<"Hello World"<<endl;
    }
};
class b :public virtual a
{
    public:
    //void geating()
    //{
    //    cout<<"My name pratham"<<endl;
    //}
};
class c :public virtual a
{
    public:
    void geating()
    {
    cout<<"World is changing"<<endl;
    }
};
class d:public c,public b
{
    public:
    /*void geating()
    {
   // cout<<"No one know what happen"<<endl;
    }*/
};
int main()
{
a ax;
b bx;
c cx;
d dx;
ax.geating();
bx.geating();
cx.geating();
dx.geating();
return 0;
}