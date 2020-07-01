//c program that append multiple lines 
#include <stdio.h>

int main ()
{
  FILE * fptr;  //declare pointers and variables
  int i,n;
  char str[100];
  char fname[20];
  char str1;
  
	printf(" Input the file name to be opened : "); //Scan the name of the file that is going to be modified.
	scanf("%s",fname);		
    fptr = fopen(fname, "a");   //open the file.
    printf(" Input the number of lines to be written : ");  //Type the number of lines that would be append
    scanf("%d", &n);
    printf(" The lines are : \n");  //Type the content that would be append.
    for(i = 0; i < n+1;i++)
    {
    fgets(str, sizeof str, stdin);  //The content is append.
    fputs(str, fptr);
  }
  fclose (fptr);
//Read the content of the text 
	fptr = fopen (fname, "r");  
	printf("\n The content of the file %s is  :\n",fname);
	str1 = fgetc(fptr);
	while (str1 != EOF)
		{
			printf ("%c", str1);
			str1 = fgetc(fptr);
		}
    printf("\n\n");
    fclose (fptr);
  return 0;
}
//w3resource.com