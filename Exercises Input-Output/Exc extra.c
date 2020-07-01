//c program that reads numbers and write the fizzbuzz test in other files.
#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fptrin; 
    FILE *fptrfb;   //declare pointers.
    FILE *fptrf;
    FILE *fptrb;
    FILE *fptrnum; 
    int i;     //declare variables
    fptrin = fopen("numbers.txt", "r");
    fptrfb = fopen("Fizzbuzz.txt", "w");    //open the files   
    fptrf = fopen("Fizz.txt", "w");
    fptrb = fopen("Buzz.txt", "w"); 
    fptrnum = fopen("NoFB.txt", "w");
    if(fptrin == NULL || fptrfb == NULL || fptrf == NULL || fptrb == NULL || fptrnum == NULL){
        printf("Unable to open the file");  //If the pointers are equal to null the program will not work.
        exit(8);
    }
    printf("Reading numbers\n");
    while(fscanf(fptrin, "%i", &i) != -1){  //scan the numbers of the file.
        if(i % 5 == 0 && i % 3 == 0){
            fprintf(fptrfb, "%i\n", i); //if the scanned number is divided by 5 and 3 correctly put the number in the file called fizzbuzz.
        }else if(i % 3 == 0){
            fprintf(fptrf, "%i\n", i);  //if the scanned number is divided by 3 correctly put the number in the file called fizz.
        }else if(i % 5 == 0){
            fprintf(fptrb, "%i\n", i);  //if the scanned number is divided by 5 correctly put the number in the file called buzz.
        }else{
            fprintf(fptrnum, "%i\n", i);    //if the scanned number does not met any condition put the number in the file called nofb.
        }
    }
    fclose(fptrin);
    fclose(fptrfb);
    fclose(fptrf);
    fclose(fptrb);
    fclose(fptrnum);    //close the files.

    printf("Numbers written succesfully");
}
//Previous homework of the teacher