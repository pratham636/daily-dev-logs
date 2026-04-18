#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream out;
    out.open("sample.txt");
    out<<"My name is pratham.\n";
    out<<"Hello everyone.\n";
    out<<"Destriy eveyone\n";
    out.close();
    ifstream in;
    string s;
    in.open("sample.txt");
    while(in.eof()==0)
    {
        getline(in,s);
        cout<<s<<endl;
    }
    return 0;
}