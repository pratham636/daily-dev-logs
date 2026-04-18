#include <stdio.h>
#include<string.h>
int check(char s[],char a[],int x,int y)
{
    int i,p=0;
    for(i=x;i<=y;i++)
    {
        a[p]=s[i];
        p++;
    }
    a[p]='\0';
    int c=1;
    int j=0;
    while(j<=(strlen(a)/2))
    {
        if(a[j]!=a[strlen(a)-j-1])
        {
            c=0;
        }
        j++;
    }
    return c;
}
int main()
{
    char s[50];
    scanf("%s",s);
    char a[50];
    int i,j,c=0;
    for(i=0;i<strlen(s);i++)
    {
        for(j=i;j<strlen(s);j++)
        {
            int b=check(s,a,i,j);
            if(b==1)
            {
                c++;
            }
            
        }
    }
    printf("%d",c);
  return 0;
}
