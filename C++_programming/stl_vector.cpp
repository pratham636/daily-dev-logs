#include<iostream>
#include<vector>
using namespace std;
template<class T>
void display(vector<T> &v)
//void display(vector<int> &v)
{
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<" ";
    }
}
int main()
{
    vector<int>vec1;
    int element,size,i;
    cout<<"Enter the size of element : "<<endl;
    cin>>size;
    for(i=0;i<size;i++)
    {
        cout<<"Enter the element : ";
        cin>>element;
        vec1.push_back(element);
    }
    vector<int>::iterator iter=vec1.begin();
    vec1.insert(iter,8);
        display(vec1);
        //vector<int>vec2(4);
        //vector<int>vec3(vec2);
        //vector<int>vec4(6,3);
        //display(vec4);
    return 0;
}