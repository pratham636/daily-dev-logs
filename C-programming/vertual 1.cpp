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
class b : public a
{
    public:
    void geating()
    {
        cout<<"My name pratham"<<endl;
    }
};
class c : public a
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
    void geating()
    {
    cout<<"No one know what happen"<<endl;
    }
};
int main()
{

return 0;
}