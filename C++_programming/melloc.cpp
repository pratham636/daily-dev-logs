#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
        int *ptr,i,n;
        cin>>n;
        ptr=(int *)malloc(n*sizeof(int));
        for(i=0;i<n;i++)
        {
            cin>>ptr[i];
            }
        for(i=0;i<n;i++)    cout<<ptr[i]<<endl;
        
    return 0;
}