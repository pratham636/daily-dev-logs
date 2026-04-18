#include<iostream>
using namespace std;
template <class T>
class Harry
{
    public:
    T data;
    Harry (T a)
    {
        data=a;
    }
    void display();
    /*{
        cout<<data;
    }*/
};
template <class T>
void Harry<T> :: display()
{
    cout<<data;
}
template <class T>
void fun(T a)
{
    cout<<endl<<a;
}
int main()
{
Harry<int>h(3);
cout<<h.data<<endl;
h.display();
fun(4.49803);
    return 0;
}