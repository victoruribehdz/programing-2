/*
DESCRIPTION:
Write a program to play "Paper, Rock or Scissors*/


#include <stdio.h>
#include <time.h>
int main (void){
	int option, ramdo=0;  // Option is the input, rmdo is where my random data is gonna save
	srand(time(NULL)); // This is to generate random variables
	
	do{ // Filter so that it never gives me zero because whenever it gives me 0 it repeats it again
		ramdo= rand()% (3+1); // Get an integer random number between zero and 3. I write +1 because I want: 0 or 1 or 2 or 3
	}while (ramdo == 0); // I put this in a do while because I am NOT INTERESTED in my zero
	printf("%d",ramdo); // Print my value for your consideration
	
	//INSTRUCTIONS:
	printf("      | Paper, Rock and Scissors Game! |\n");
    printf("\n    **** Instructions:****\n");
    printf("\n***Rock breaks scissors, the life counter will be reduce by one.");
    printf("\n***Paper envolves rocks, the life counter will be reduced by one.");
    printf("\n***Scissors cuts paper, the life counter will be reduced by one\n");
    printf("\n***With same element you have to repeat\n");
    printf("\n>>YOU HAVE ONLY ONE CHANCES, GOOD LUCK\n");
    
    do { //The rule says that if the two players have the same, elements are chosen again
	printf ("\nChoice an option: \n1:Rock  \n2:Paper  \n3:Scissors\n Option---->>>>>> ");	scanf("%d", &option);
	} while (option == ramdo); //If the player's choice is equal to that of the machine: repeat until it is not true
	
	//Option where user wins
	if (option == 1 &&  ramdo == 3){ // rock vs scissors = ROCK
		printf ("\nYou: %d vs Machine: %d\n",option, ramdo);
		printf("\nYOU WINE!");
	}
	else if (option == 2 &&  ramdo == 1){ //Paper vs Rock = Paper
		printf ("\nYou: %d vs Machine: %d\n",option, ramdo);
		printf("\nYOU WINE!");
	}
	else if (option == 3 &&  ramdo == 2){ // Scissors vs Paper = Scissors
		printf ("\nYou: %d vs Machine: %d\n",option, ramdo);
		printf("\nYOU WINE!");
	}
	
	//Options where machine wins
	else {
		printf ("\nYou: %d vs Machine: %d\n",option, ramdo);
		printf("\nYou lose!, MACHINE IS THE WINNER");
	}
	
	return 0;
	
}
