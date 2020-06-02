# Subprograms and Recursions

## [Subprograms](https://www.geeksforgeeks.org/subprogram-and-its-characteristics/)
A Subprogram is a program inside any larger program that can be reused any number of times.

### Characteristics of a Subprogram
1. A Subprogram is implemented using the Call & Return instructions in Assembly Language.
2. The Call Instruction is present in the Main Program and the Return Instruction is present 
in the subprogram itself.
![Call & Return](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-drawing-5-2.jpg)
3. The Main Program is suspended during the execution of any subprogram. 
4. For the implementation of any subprogram, a “Stack” is used to store the “Return Address” to the Main Program .
5. The Main advantage of Subprogram is that it avoids repetition of Code and allows us to reuse the 
same code again and again.
### Exchange of parameters in Subprograms
* Formal Parameter : A variable and its type as they appear in the prototype of the function or method.
* Actual Parameter : The variable or expression corresponding to a formal parameter that appears in the function or method call in the calling environment.
* Modes:
  * IN: Passes info from caller to calle.
  * OUT: Callee writes values in caller.
  * IN/OUT: Caller tells callee value of variable, which may be updated by callee.

1. By Reference: This technique uses in/out-mode semantics. Changes made to formal parameter do
 get transmitted back to the caller through parameter passing. Any changes to the formal parameter are 
 reflected in the actual parameter in the calling environment as formal parameter receives a reference 
 (or pointer) to the actual data. 
```
#include <stdio.h> 

void swapnum(int* i, int* j) 
{ 
	int temp = *i; 
	*i = *j; 
	*j = temp; 
} 
int main(void) 
{ 
	int a = 10, b = 20; 
	printf("a is %d and b is %d\n", a, b); 
	return 0; 
} 
```
2. By Value: This method uses in-mode semantics. Changes made to formal parameter do not get 
 transmitted back to the caller. Any modifications to the formal parameter variable inside the called 
 function or method affect only the separate storage location and will not be reflected in the actual 
 parameter in the calling environment.
```
#include <stdio.h> 

void func(int a, int b) 
{ 
	a += b; 
	printf("In func, a = %d b = %d\n", a, b); 
} 
int main(void) 
{ 
	int x = 5, y = 7;  
	func(x, y); 
	printf("In main, x = %d y = %d\n", x, y); 
	return 0; 
} 
```
