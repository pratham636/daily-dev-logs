#include<bits/stdc++.h>
using namespace std;
int n,x,i;
int a[1000020];
int p[1000020];
int f[1000020];
int main()
{
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>x;
        p[x]=i;
        cout<<"P[x]"<<p[x]<<" x"<<x<<endl;
    }
    cout<<endl<<endl;
    for(i=0;i<n;i++)
    {
    scanf("%d",&x);
        a[i]=-p[x]-1;
        cout<<"x"<<x<<" a[i]"<<a[i]<<endl;
    }
    for(i=0;i<n;i++)
        *lower_bound(f,f+n,a[i])=a[i];
        cout<<
    int zero=0;
    printf("%ld\n",lower_bound(f,f+n,zero)-f);
    return 0;
}