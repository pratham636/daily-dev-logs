#include<iostream>
using namespace std;
class base
{
    
 public:
    virtual void get()
    {
    cout<<"1 base class call"<<endl;
    }
};
class deriver : public base
{
 public:
    void get()
    {
        cout<<"2 deriver class call"<<endl;
    }
};
int main()
{
//base obj_base;
//base *base_pointer=&obj_base;

base *base_pointer;
base obj_base;
deriver obj_deriver;
base_pointer=&obj_deriver;
base_pointer->get();
    return 0;
}