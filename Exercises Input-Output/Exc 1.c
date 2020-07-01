//C program to create a file
#include <stdio.h>
#include <stdlib.h>

#define size_array 1000

int main(){
    char str[size_array];   //declare varianles and pointers
    FILE *fptr;
    fptr = fopen("Lasagna.txt", "w");   //In this part you put the name of the file

    if(fptr == NULL){
        printf("Unable to create the file\n");  //If the ptr is equal to null, print error
        exit(8);
    }else{
        printf("Type the information for the file: \n");    //In this part the user write the content of the file
        fgets(str, size_array, stdin);
        fputs(str, fptr);
    }
    fclose(fptr);
    printf("The file has been created succesfully\n");  //The program said that the file has been created.
}
//w3resource.com