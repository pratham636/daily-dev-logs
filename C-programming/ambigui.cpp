#include<iostream>
using namespace std;
class a 
{
    public:
    void get()
    {
        cout<<"hello world"<<endl;
    }

};
class b 
{
    public:
    void get()
    {
        cout<<"None"<<endl;
    }
};
class c : public  a , public b 
{
    public:
    void get()  
    {
        cout<<"Welcome man"<<endl;
       // b::get();
    }
};

int main()
{
    a ax;
    b bx;
    c cx;
    ax.get();
    bx.get();
    cx.get();
    return 0;
}