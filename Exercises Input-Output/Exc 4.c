//c program that reads the file
#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fptr; //declare pointers and variables
    char fname[30];
    char str;
    printf("Type the filename that is going to be openned: ");  //Write the name of the file
    scanf("%s", fname);
    fptr = fopen(fname, "r");   //The name of the file is equal to the pointer
    if(fptr == NULL){   //If ptr is equal to null, print error
        printf("Unable to open the file\n");
        exit(8);
    }   //print the content of the file.
    printf("\nThe contentof the file %s is: \n, fname); 
    str = fgetc(fptr);
    while(fptr != EOF){ 
        printf("%c", str);
        str = fgetc(fptr);
    }
    fclose(fptr);  
    printf("\n\n");
}

//w3resource.com