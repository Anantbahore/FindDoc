#include<stdio.h>
int main(){
    int n,k;
    printf("enter the number:");
    scanf("%d",n);
    for(int i=0;i<n;i++){
        if(n%2==0){printf("2");
        n=n/2;
        }
        if(n%3==0){
            printf("3");
            n=n/3;
        }
        if(n%5==0){
            printf("5");
            n=n/5;
        }
        if(n%7==0){
            printf("7");
            n=n/7
        }
       else{ k=n;}
    
    }
    printf{"%d",&k;}
}