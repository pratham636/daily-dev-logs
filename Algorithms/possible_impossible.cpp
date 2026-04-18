#include <bits/stdc++.h>
using namespace std;
int p = 1, n, j=0, a[105];
char c;
int main()
{
    a[j++] = 1;
    while (cin>>c && c != '=')
    {
        if (c == '-') p--; a[j++] = -1; cout<<"p "<<p<<" j"<<j<<" a[j] "<<a[j]<<endl;
        if (c == '+') p++; a[j++] = 1; cout<<"p "<<p<<" j"<<j<<" a[j] "<<a[j]<<endl;
    }
    cin>>n;
    cout<<"\nn "<<n;
    for(int i=0;i<j;i++)
    {
        if(a[i]>0)while (p<n && a[i]<n) a[i]++; p++;
        else while (p>n&&a[i]<0 && a[i]>-n) a[i]--; p--;
    }
    if (p != n) { cout << "Impossible\n"; return 0; }
    cout << "Possible\n";
    for(int i=0;i<j;i++)
    cout << (i ? (a[i]<0 ? "- " : "+ ") : "") << abs(a[i]) << " ";
    cout << "= " << n;
    return 0;
}