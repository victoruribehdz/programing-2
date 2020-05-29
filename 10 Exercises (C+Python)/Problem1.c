/*Write a program to input any character and check whether it is alphabet, digit or
special character.*/
// Expected Output: A is alphabet
#include <stdio.h>

int main(){
    char ch;    //Declare your variable
    printf("Type a character: ");
    scanf("%c", &ch);   //Scan the value that is type by the user
    if((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')){   //If you type a letter print alphabet
        printf("'%c' is alphabet", ch);
    }else if(ch >= '0' && ch <= '9'){ //If not type a letter but type a number print digit 
        printf("'%c' is a digit", ch);
    }else{
        printf("'%c' is a special character", ch);  //Else print special character
    }
    return 0;
}