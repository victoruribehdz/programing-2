/*
DESCRIPTION:
Write a program that display the Zodiacal Sign using the day and month of birth. */

#include <stdio.h>
int main (){
	int day, month; //To save the values of the birthday 
	
	printf("      |Welcome, this program is to know your zodiacal sign according your birthday|      \n");
	printf ("Please write the DAY and dont try to write a 0 before: \n"); scanf("%d",&day); //input
	printf("Write the MONTH and dont try to write a 0 before: \n"); scanf("%d",&month); //input
	
							//Options of zodiacal sign
	
	//Aquarius: January 20th- Feb 18th
	if ((month==1 && day>=22)||(month==2 && day<=18)){
		printf("You are: Aquarius");
	}
	//Pisces: Feb 19th- March 20th
	else if ((month==2 && day>=19)||(month==3 && day<=20)){
		printf("You are: Pisces");
	}
	//Aries: March 21th - Ap 20th
	else if ((month==3 && day>=21)||(month==4 && day<=20)){
		printf("You are: Aries");
	}
	//Taurus: Ap 20th - May 20th
	else if ((month==4 && day>=20)||(month==5 && day<=20)){
		printf("You are: Taurus");
	}
	
	//Geminis: Mmay 21th- June 20th
	else if ((month==5 && day>=21)||(month==6 && day<=20)){
		printf("You are: Gemini");
	}
	//Cancer: June 21th- July 22nd
	else if ((month==6 && day>=21)||(month==7 && day<=22)){
		printf("You are: Cancer");
	}
	
	//Leo: July 23rd - Aug 22nd
	else if ((month==7 && day>=23)||(month==8 && day<=22)){
		printf("You are: Leo");
	}
	//Virgo: Aug 23rd - Sep 22nd
	else if ((month==8 && day>=23)||(month==9 && day<=22)){
		printf("You are: Virgo");
	}
	//Libra: Sep 23rd - Oct 22nd
	else if ((month==9 && day>=23)||(month==10 && day<=22)){
		printf("You are: Libra");
	}
	//Scorpio: Oct 23rd - Nov 21st
	else if ((month==10 && day>=23)||(month==11 && day<=21)){
		printf("You are: Scorpio");
	}
	//Saggitarious: November 22nd - Dec 21st
	else if ((month==11 && day>=22)||(month==12 && day<=21)){
		printf("You are: Saggitarious");
	}
	//Capricorn: Dec 22nd - Janu 19th
	else if ((month==12 && day>=22)||(month==1 && day<=19)){
		printf("You are: Capricorn");
	}
	return 0;
}
