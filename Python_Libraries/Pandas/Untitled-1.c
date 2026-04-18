#include<stdio.h>
#include<string.h>
int z=0,i=0,j=0,c=0;
char a[16],ac[20],stk[15],act[10];
void check();
int main()
   {

      puts("GRAMMAR is S->CC \n C->cC \n C->d");
      puts("enter input string ");
      scanf("%s",a);
      c=strlen(a);
      strcpy(act,"SHIFT->");
      puts("stack \t input \t action");
      for(i=0; j<c;i++,j++)
       {
         if(a[j]=='d'||a[j]=='c')
           {
              stk[i]=a[j];
              stk[i+2]='\0';
              a[j]=' ';
              printf("\n$%s\t%s$\t%sid",stk,a,act);
              check();
           }
         else
           {
              stk[i]=a[j];
              stk[i+1]='\0';
              a[j]=' ';
              printf("\n$%s\t%s$\t%ssymbols",stk,a,act);
              check();
           }
       }

   }
void check()
   {
     strcpy(ac,"REDUCE TO E");
     
     for(z=0; z<c; z++)
       if(stk[z]=='d')
         {
           stk[z]='C';
           stk[z+1]='\0';
           printf("\n$%s\t%s$\t%s",stk,a,ac);
           i=i-1;
         }
     for(z=0; z<c; z++)
       if(stk[z]=='C' && stk[z+1]=='C')
         {
           stk[z]='S';
           stk[z+1]='\0';
           printf("\n$%s\t%s$\t%s",stk,a,ac);
           i=i-1;
         }
     for(z=0; z<c; z++)
       if(stk[z]=='c' && stk[z+1]=='C')
         {
           stk[z]='C';
           stk[z+1]='\0';
           stk[z+1]='\0';
           printf("\n$%s\t%s$\t%s",stk,a,ac);
           i=i-1;
         }
   }