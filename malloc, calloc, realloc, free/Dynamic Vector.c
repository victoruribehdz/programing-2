#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void random(int *vector, int N);    //use the struture

int main(){ //declare variables
    int i, j, k;
    int N = 10;
    int *vector;    //declare the pointer
    vector = (int)malloc(N*sizeof(int));    //asign the memory space for the variable
    if(vector == NULL){
        printf("Memory space could not be reserved.\n") //if it's not enough space print this phrase
    } else {
        random(vector, N);  //start with the process
        for(i = 0; i < N, i++){
            j = i + 1;
            while(j < N){
                if(*(vector+i) == *(vector+j)){
                    for(k = j; k+1 < N; k++){
                        *(vector+k) = *(vector+k+1); 
                    }
                    N--;
                }
                else{
                    j++;
                }
            }
        }
        vector = (int*)realloc(N*sizeof(int));  //reasegn the memory space
        if(vector == NULL){
            printf("Memory space could not be reserved.\n") //if it's not enough space print this phrase
        } else {
            for(i = 0; i < N; i++){
                printf("%i, ", *(vector+i));
            }
            printf("\n");   //print the results
        }
    }
    system ("pause\n");
    return 0;
}

void random(int *vector, int N){    //create the structure that we use
    int i;
    srand(time(NULL));
    for(i = 0; i < N; i++){
        *(vector+i) = rand() % 3;
        printf("%i, ", *(vector+i));
    }
    printf("\n");
}