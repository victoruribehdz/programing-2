//Exercise 13-2: Write a function that takes a single string as its argument and returns a pointer to the first 
//nonwhite character in the string.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *nonwhite(char *string);    //finds first nonwhite character in a string

int main(){
    char string[] = " This is an example string";
    printf("First non white character in the string is: '%c'\n", *nonwhite(string));
    return 0;
}
/* nonwhite -- finds first nonwhite character in a string
 
    Argument
    string -- string to investigate
    Return
    pointer to first non white character in string
*/
char *nonwhite(char *string){
    //Loop through all string characters
    while(*string != '\0'){
        //Check if the character is nonwhite
        if(! isspace(*string)){
            // Return pointer to this first nonwhite character
            return string;
        }
        ++string;
    }
    return string;
}