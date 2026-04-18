#include<stdio.h>
#include<string.h>
int main()
{
char a[100],b[100],c[100];
scanf("%s\n%s",&a,&b);
printf("\n\n%s\n%s\n",a,b);
strcat(a,b);
printf("%s",a);
strcpy(c,a);
printf("\n%s\n%d",c,strlen(a));
printf("%d %d",strcmp(a,c),strcmp(c,b));
    return 0;
}