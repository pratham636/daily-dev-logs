#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
        int *ptr,i,n;
       cout<<"Enter size of number : "<<endl;
        cin>>n;
        ptr=(int *)calloc(n,sizeof(int));
        for(i=0;i<n;i++)
        {
            cin>>ptr[i];
            }
        for(i=0;i<n;i++)    cout<<ptr[i]<<endl;
       
       cout<<"Enter size of number : "<<endl;
        cin>>n;
          ptr=(int *)realloc(ptr,n*sizeof(int));
        for(i=0;i<n;i++)
        {
            cin>>ptr[i];
            }
            for(i=0;i<n;i++) cout<<*(ptr+i)<<endl;

            free(ptr);
                        for(i=0;i<n;i++) cout<<*(ptr+i)<<endl;

    return 0;
}