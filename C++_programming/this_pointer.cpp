#include<iostream>
using namespace std;
class class1
{
int a;
public:
    void set(int a)
    {
        this->a=a;
    }
    void get()
    {
        cout<<a;
    }
};
int main()
{
    class1 ca;
    ca.set(4);
    ca.get();
    return 0;
}