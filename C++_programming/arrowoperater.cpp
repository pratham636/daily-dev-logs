#include<iostream>
using namespace std;
class complex
{
    int x,y;
    public:
    void gerdata()
    {
            cout<<x<<endl<<y;
    }
    void setdata(int a,int b)
    {
        x=a;
        y=b;
    }
};
int main()
{
    //complex a;
    //complex *ptr=&a;
    complex *ptr=new complex;   
    //(*ptr).setdata(3,5);
    //(*ptr).gerdata();
    ptr->setdata(4,5);
    ptr->gerdata();
    //a.setdata(4,7);
    //a.gerdata();
    return 0;
}
