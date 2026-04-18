#include <iostream>
using namespace std;
int main(){
	string s,t;
    std::cin>>s>>t;
	int o = s.find(t);
    cout<<"o1 "<<o<<endl;
	int c =0;
	while(o!=-1){
		c++;
		o = s.find(t,o+t.length());
        cout<<"o2 "<<o<<endl;
	}
	cout<<c<<endl;
}