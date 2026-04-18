#include <iostream>
using namespace std;
class base
{
    public:
    int var_base;
    virtual void display()
    {
        cout<<"Display base class :"<<var_base<<endl;
    }
};
class deriver : public base 
{
    public:
    int var_deriver;
    void display()
    {
        cout<<"Display base class :"<<var_base<<endl;
        cout<<"Display deriver class :"<<var_deriver<<endl;
    }
};
int main()
{
base *var_base_pointer;
base obj_base;
deriver obj_deriver;
var_base_pointer = &obj_deriver;
var_base_pointer->var_base=43;
//var_base_pointer->var_deriver=23;    error
var_base_pointer->display();
deriver * var_deriver_pointer;
var_deriver_pointer =& obj_deriver;
var_deriver_pointer->var_base=90;
var_deriver_pointer->var_deriver=23;
var_deriver_pointer->display();
    return 0;
}