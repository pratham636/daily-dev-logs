#include<stdio.h>
int main()
{
    int x[100],i,*u;
    u=&x[0];
    //int *u=x;
    for(i=0;i<5;i++)  {scanf("%d",&x[i]);}
    for(i=0;i<5;i++) {printf("%d ",*(u+i));}
    int a=9;
    int *b=&a;
    int **c=&b;
    printf("\n%d %d %d",a,*b,**c);
    printf("\n%d %d %d",&a,b,*c);
    printf("\nnull %d %d",&b,c);
    return 0;
}
