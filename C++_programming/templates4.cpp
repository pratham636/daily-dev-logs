#include<iostream>
using namespace std;
template<class T>
void swapp(T &x,T &y)
{
    T temp= x;
    x=y;
    y=temp;
}
template<class T1,class T2>
float funavr(T1 a,T2 b)
{
    float avg=(a+b)/2;
    return avg;
}

int main()
{
    float a;
    a=funavr(88,4);
    cout<<a<<endl;
    int x=4,y=2;
    swapp(x,y);
    cout<<x<<endl<<y;
    return 0;
}