//Write a program to check whether a number is even or odd.
//Expected Output: Even or Odd
#include <stdio.h>
#include <stdlib.h>

int main (){
    int x;  //Declare the variable
    scanf("%d", &x);    //Scan and asign a value to the variable
    if (x % 2 == 0){    //If the number can be divided by 2 and the residue is O print even
        printf("Even");
    } else{ //Else print odd
        printf("Odd");
    }
    return 0;
}