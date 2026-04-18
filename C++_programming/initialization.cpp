#include<iostream>
using namespace std;
class name
{
    int a;
    int b;
    public:
    name(int i,int j):a(i*j),b(j)
    //name(int i,int j):a(i*2),b(j*4) do whith any constant
    //name(int i,int j):a(i*j),b(j*i)
    //name(int i,int j):a(i),b(j*a)
    {
        cout <<"a"<<a<<endl<<"b"<<b<<endl;
    }
};
int main()
{
    int a,b;
    cin>>a>>b;
    name so(a,b);
    return 0;
}