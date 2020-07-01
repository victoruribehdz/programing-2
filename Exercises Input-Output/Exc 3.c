//c program that read a file with numbers and create files with odd and even.
#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fptrin;   //declare pointers
    FILE *fptrodd; 
    FILE *fptreven; 
    int i;  //declare variables
    fptrin = fopen("numbers.txt", "r"); 
    fptrodd = fopen("Oddnumbers.txt", "w");     //open the files.
    fptreven = fopen("Evennumbers.txt", "w");

    if(fptrin == NULL || fptrodd == NULL || fptreven == NULL){
        printf("Unable to open the file");  //If the pointers are equal to null the program will not work.
        exit(8);
    }
    printf("Reading numbers\n");
    while(fscanf(fptrin, "%i", &i) != -1){      //scan the numbers of the file.
        if(i % 2 == 0){
            fprintf(fptreven, "%i\n", i);   //if the number scanned is divide by 2 and the residual is 0 put in the file of even numbers.
        }else{
            fprintf(fptrodd, "%i\n", i);    //if not put the number in the file odd numbers.
        }
    }
    fclose(fptrin);
    fclose(fptrodd);    //close the file
    fclose(fptreven);

    printf("Numbers written succesfully");
}
//Previous homework of the teacher