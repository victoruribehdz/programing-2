//Exercise 13-1: Write a program that uses pointers to set each element of an array to zero.
#include <stdio.h>
#define MAX_NUMBERS 5

int main(){
    int numbers[MAX_NUMBERS] = { 1, 2, 3, 4, 5 };   //define the array
    int *numbers_ptr;   //pointer to number array
    for(numbers_ptr = &numbers[0]; numbers_ptr < &numbers[MAX_NUMBERS]; ++numbers_ptr){
        *numbers_ptr = 0;   //If the conditions are met the pointer would be equal to 0
    }
    int counter;    
    for(counter = 0; counter < MAX_NUMBERS; ++counter){
        printf("numbers[%d] = %d\n", counter, numbers[counter]);    //If the condition is met print the array, but replace the numbers with 0
    }
    return 0;
}