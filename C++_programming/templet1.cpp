#include<iostream>
using namespace std;
template <class T>
class vector
{
    public:
    T *arr;
    //int *arr;
    int size;
    vector(T m)
    //vector(int m)
    {
        size=m;
        arr= new T [size];
        //arr= new int [size];
    }
    
    T dotproduct(vector &v)
    //int dotproduct(vector &v)
    {
        T d=0;
        //int d=0;

        for (int i = 0; i < size; i++)
        {
            cout<<"this v "<<this->arr[i]<<" v "<<v.arr[i]<<endl;
            d+=this->arr[i]* v.arr[i];
        }
        return d;
    }
};
int main()
{
        vector<float> v1(3);
        //vector v1(3);
        v1.arr[0]=6.89;
        v1.arr[1]=26.890;
        v1.arr[2]=16.56;
        vector<float> v2(3);
        //vector v2(3);
        v2.arr[0]=9.34;
        v2.arr[1]=29.23;
        v2.arr[2]=39.567;
        float a=v1.dotproduct(v2);
        //int a=v1.dotproduct(v2);
        cout<<a<<endl;
    return 0;
}