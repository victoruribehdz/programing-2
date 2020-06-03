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
## [Recursion](https://www.geeksforgeeks.org/recursion/)
Recursion is that property that has a function by which that function can call itself. Recursion can be used as an alternative to iteration. A solution in italics is usually more efficient in terms of computer time than an iterative solution due to the auxiliary operations that they carry with them.
Supplementary function calls however, in many circumstances the use of recursion allows programmers to specify natural, simple solutions that would otherwise be difficult to solve. For this reason, recursion is a powerful and important tool in problem solving and programming.
   
   ![Recursion](https://i.ytimg.com/vi/vLhHyGTkjCs/maxresdefault.jpg)

### The nature of recursion.

The programs so far eliminated, generally structured, are made up of a series of functions that call each other in a disciplined way. In some problems it is useful to have functions that call themselves. A recursive subprogram is a subprogram that calls itself either directly or indirectly to recursion. It is an important topic frequently discussed in programming and introductory computer science courses.

### Direct recursion in indirect.

In direct recursion the code of the recursive applet F contains a statement that invokes F, while an indirect recursion the applet F invokes the applet G which in turn invokes the applet P and so on until the applet F is invoked again.

### Direct recursion.
If a function, procedure, or method invokes itself, the process is called a direct recursion function, procedure, or method can invoke a second function, procedure, or method that its v invokes the first, this process is known as indirect recursion or mutual.

A requirement for a recursive algorithm to be correct is that it does not generate an infinite sequence of calls on itself. Any algorithm that generates such a sequence can never end. Consequently, the recursive definition must include a base component (output condition) in which end) is directly defined (i.e. not recursively) for one or more values of n.

There must be a "way out" of the recursive call sequence. So in function f(n) = n! para n entero. 

**In the case of the Fibonacci series:**
*F0= 0 
F1= 1* 
Fn= Fn-1 + Fn-2

>>>F=0 F=1<<<
They constitute the base component or exit conditions Fn =Fn-1 Fn-2. 
Example c:
```
#include <stdio.h>
int fibonnaci (int n);
int main (){
	int numero, i;
	printf ("Digite hasta que numero desea la serie: ");	scanf("%d",&numero);
	
	for (i=0; i<numero; i++){ //Paso dos
		printf("%d ", fibonnaci(i));
	}
	
	return 0;
}
int fibonnaci (int n){ // paso uno; aquí estás pidiendo la varibale
	// 0 1 1 2 3 5 8 13...
	if (n==0 || n==1){ //caso base
		return n;
	}
	else {
		return (fibonnaci(n-1)+ fibonnaci(n-2)); //porque necesitamos sumar los dos numeros anteriores
	}
} 
```
### Python example:
```
x=19
def fibo(num)
	if num <=1: ##base case
		return num
	else:
		return (fibo(num-1) + fibo(num-2))
		
	if x<=0:
		printf("Please enter a positive number");
	else:
		printf("Fibonacci series: ")
		for i in range(x):
			print(fibo(i))
```
### Indirect recursion

Indirect recursion occurs when one applet calls another. which will eventually end up calling the first one again.

**C example:**
 Ej: Par o Impar:
 ```
      int par( int nump )
      {
          if(nump==0) return(1);
          return( impar(nump-1));
      }
 
      int impar( int numi )
      {
          if(numi==0) return(0);
          return( par(numi-1));
      }
```
**Python example:**
```
def odd(n):
 if n <= 10:
 return n+1
 n = n+1
 even(n)
 return
def even(n):
 if n <= 10:
 return n-1
 n = n+1
 odd(n)
 return
```
### Recursion termination condition

When implementing a recursive subprogram, it will be necessary to consider a termination condition, otherwise the subprogram would continue to call itself indefinitely and there would come a time when the memory could run out. Consequently, it would be necessary to establish in any recursive applet the stop condition that ends the recursive calls and to avoid the calls indefinitely. Thus, for example, in the case of the factorial function defined above, the output condition can be when the number is 1 or 0, since in both cases the factorial is 1.



