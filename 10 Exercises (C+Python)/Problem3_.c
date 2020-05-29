//Write a program to find maximum between three numbers.
//Expected Output: The maximum number is the first

#include <stdio.h> 
#include <math.h>
#include <stdlib.h>


main(){
int a,b,c; //Declare three variables
printf("Write 3 numbers:\n ");	scanf(" %d %d %d",&a,&b,&c); // Ask for 3 num, a, b y c

if(a<b){ //Compare a is greater than b
	if (a<c){ //c is greater than a
		if (b<c){ //c is greater than b
			printf("%d %d %d\n\n", a,b,c);
			printf("The maximum values is: %d", c);
		}
		else{ //b is greater than c
			printf("%d %d %d\n\n", a,c,b);
			printf("The maximum values is: %d", b);
		}
	}
	else{ 	//a is greater than c
		printf("%d %d %d\n\n", c,a,b);
		printf("The maximum values is: %d", b);
	}
}

else // b is greater than a
{
	if (a<c){ //c is greater than a
		printf("%d %d %d\n\n", b,a,c);
		printf("The maximum values is: %d", c);
	}
	else{ //a is greater than c
		if (c<b){ //b is greater than c
		printf("%d %d %d\n\n", c,b,a);
		printf("The maximum values is: %d", a);
		}
		else{ // c is greater than b
		printf("%d %d %d\n\n", b,c,a);
		printf("The maximum values is: %d", a);
		}
	}
	return 0;
}
}
