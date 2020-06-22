#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
  printf("Type a string: ");  //The user type the string
  int i, size = 0;
  char *cadena = calloc(1, 1); //asign space for the memory and the number of elements that would be store in this pointer
  scanf("%[^\n]", cadena); 
  size = strlen(cadena);
  char *auxCadena = calloc(size+1, 1);
  memset(auxCadena, '\n', size); // by the memsets all the characters will be \n
  for(i = 0; i < size; i++){
    if(cadena[i] == 32){
      continue;
    } else{
      auxCadena[i] = cadena[i];
  for(i = 0; i < size; i++){ 
    if(auxCadena[i] != '\n'){ 
      printf("%c", auxCadena[i]);
    }
  }
  printf("\n"); 
  }
}