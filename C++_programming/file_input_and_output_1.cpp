#include<iostream>
#include<fstream>
using namespace std;
int main()
{ 
    //write
    string st="Today is great day.";
    ofstream out("sample.txt");
    out<<st;
   //read
   out.close();
   string st2,st3;
   ifstream in("sample.txt");
   //in>>st2;
   getline(in,st2);
   getline(in,st3);
   cout<<st2<<endl<<st3;
 return 0;
}