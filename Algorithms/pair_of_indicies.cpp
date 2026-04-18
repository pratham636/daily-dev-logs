#include <iostream>
#include <map>
using namespace std;
#define N 10000000
int n,a[N],c[N],w;
void upd(int i,int c){

}
int main(){
  cin>>n;
  for(int i=0;i<n;++i)cin>>a[i];
  map<int,int>u,v;
  for(int i=n;i-->0;){
    cout<<"i"<<i<<endl;
    int x=++u[a[i]];
    cout<<"u[a[i]]"<<u[a[i]]<<endl;
    while(x<N)++c[x],x+=x&-x,cout<<"x "<<x<<endl;
  }

  for(int i=0;i<n;++i){
    int x=u[a[i]]--,y=v[a[i]]++;
    while(x<N)--c[x],x+=x&-x;
    while(y>0)w+=c[y],y-=y&-y;
  }
  cout<<w<<endl;
}