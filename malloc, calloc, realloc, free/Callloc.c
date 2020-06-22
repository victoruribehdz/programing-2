#include <stdio.h>
#include <stdlib.h>

int main(){
    int i = 0;
    int *ptr;
    int var;
    ptr = calloc(10, sizeof(double));
    while(i < 10){
        var = *(ptr+i);
        printf("%d\n", var);
    }
}