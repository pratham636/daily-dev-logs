#include<iostream>
#include<list>
using namespace std;
void display(list<int> &lst)
{
    list<int>::iterator it;
    for(it = lst.begin();it!=lst.end();it++)
    {
        cout<<*it<<" ";
    }
    cout<<endl; 
}
int main()
{       
    list<int>list1;
    list1.push_back(7);
    list1.push_back(7);
    list1.push_back(7);
    list1.push_back(8);
    list1.push_back(9);
    display(list1);
    
    list<int>list2(3);
    list<int>::iterator it =list2.begin();
*it=45;
it++;
*it=89;
it++;
*it=90;
it++;
 list2.push_back(7);
    list2.push_back(8);
    list2.push_back(9);
     list2.push_back(7);
    list2.push_back(8);
    list2.push_back(9);
    display(list2);
    return 0;
}