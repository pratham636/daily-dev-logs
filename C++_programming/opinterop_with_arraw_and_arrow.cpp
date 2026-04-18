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
    complex *ptr=new complex[4];   
    //(*ptr).setdata(3,5);
    //(*ptr).gerdata();
    for(int i=0;i<5;i++)
    {
    (ptr+i)->setdata(i+1,5-i);
    (ptr+i)->gerdata();
    }
    //a.setdata(4,7);
    //a.gerdata();
    return 0;
}
