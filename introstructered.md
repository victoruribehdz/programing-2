# **Introduction to structured programming**
-------------------------------------------------------------------------------------------------------------------------

## What is a paradigm?  

[Structured programming](https://searchsoftwarequality.techtarget.com/definition/structured-programming-modular-programming) sometimes known as modular programmingis a programming paradigm that facilitates the creation of programs with readable code and reusable components. All modern programming languages support structured programming, but the mechanisms of support, like the syntax of the programming languages, varies.

Where modules or elements of code can be reused from a library, it may also be possible to build structured code using modules written in different languages, as long as they can obey a common module interface or application program interface (API) specification. However, when modules are reused, it's possible to compromise data security and governance, so it's important to define and enforce a privacy policy controlling the use of modules that bring with them implicit data access rights.
According with TechTarget:
> Structured programming encourages dividing an application program into a hierarchy of modules or autonomous elements, which may, in turn, contain other such elements. Within each element, code may be further structured using blocks of related logic designed to improve readability and maintainability. These may include case, which tests a variable against a set of values; Repeat, while and for, which construct loops that continue until a condition is met. In all structured programming languages, an unconditional transfer of control, or goto statement, is deprecated and sometimes not even available.    
Programming paradigms are a way to classify programming languages based on their features.

![Varieties of paradigms](https://media.geeksforgeeks.org/wp-content/uploads/1-344.png)

## Implementation methods of the programming paradigms.
According with Edukera, we must bear in mind that both [**interpreted** and **compiled**](https://www.edureka.co/community/6776/compiled-vs-interpreted-languages) programming are codes that translate all syntax into *machine language*. In this case, you have to define what machine language is. Machine language is those instructions that the computer processor understands and is a binary code (1 and 0)
The **compiled language** requires an additional step before its execution and converts the code to machine language, in addition a compiled language is much faster than one interpreted because when it is executed it is already in machine code. In short, it is a program that transforms the source code of a program to its equivalent in another lower-level programming language.

### Examples:
1. C
2. C ++
3. JAVA.
4. Go.

The **interpreted language** is a converter to machine language as it is executed. In short, it is a program that directly executes instructions written in a given programming language and is optimized for the moment of execution.

### Examples:
1. Python.
2. Ruby.
3. JavaScript.
In conclusion, compiling is done to optimize execution work and this means more work for the programmer. In the interpreted, it is made to be easier for the programmer and this means an extra effort for the execution.

Below is an image taken from [Medium](https://medium.com/from-the-scratch/stop-it-there-are-no-compiled-and-interpreted-languages-512f84756664):
![Interpreted and compiled](https://miro.medium.com/max/991/1*3Iy-ohRRXj3lChmEbQTxIQ.png)

## [Classification of programming paradigms.](https://www.geeksforgeeks.org/introduction-of-programming-paradigms/) 

### Imperative Programming paradigm. 
It performs step by step task by changing state. The main focus is on how to achieve the goal. The paradigm consist of several statements and after execution of all the result is stored. Here an [example](https://spines.me/es/help/markdown/syntax/) of code:
```
const container = document.getElementById(‘container’);
const btn = document.createElement(‘button’);
btn.className = ‘btn red’;
btn.onclick = function(event) {
 if (this.classList.contains(‘red’)) {
   this.classList.remove(‘red’);
   this.classList.add(‘blue’);
 } else {
   this.classList.remove(‘blue’);
   this.classList.add(‘red’);
 }
};
container.appendChild(btn);
```
1. **Procedural programming paradigm:**:
  This paradigm emphasizes on procedure in terms of underlying machine model. It has the ability to reuse the code and it was boon at that time when it was in use because of its reusability.  
BASIC, Pascal and C are examples of this paradigm.  
  
2. **Object Oriented Programming:**
  The program is written as a collection of classes and object which are meant for communication. More emphasis is on data rather procedure. It can handle almost all kind of real life problems which are today in scenario. Examples: Java, JavaScript, Python, C++, Visual Basic, .NET, Ruby, Scala and PHP
  
3. **Parallel Processing approach:**
  Parallel processing is the processing of program instructions by dividing them among multiple processors. A parallel processing system posses many numbers of processor with the objective of running a program in less time by dividing them. This approach seems to be like divide and conquer.

### Declarative Programming paradigm.
Is a style of building programs that expresses logic of computation without talking about its control flow. The focus is on what needs to be done rather how it should be done basically emphasize on what code code is actually doing. It just declare the result we want rather how it has be produced. Here an [example](https://spines.me/es/help/markdown/syntax/) in a code:  
```
 class Button extends React.Component{
  this.state = { color: 'red' }
  handleChange = () => {
    const color = this.state.color === 'red' ? 'blue' : 'red';
    this.setState({ color });
  }
  render() {
    return (<div>
      <button 
         className=`btn ${this.state.color}`
         onClick={this.handleChange}>
      </button>
    </div>);
  }
}
```

1. **Logic Programming paradigm:**
  It can be termed as abstract model of computation. It would solve logical problems like puzzles, series etc. In logic programming we have a knowledge base which we know before and along with the question and knowledge base which is given to machine, it produces result.Examples: Mercury, ECLiPSe, QL, PROGOL, etc. 
  
2. **Functional Programming:**
  The functional programming paradigms has its roots in mathematics and it is language independent. The key principal of this paradigms is the execution of series of mathematical functions. The central model for the abstraction is the function which are meant for some specific computation and not the data structure. Examples:Python, Haskell, Lisp, Erlang y Clojure. 
  
3. **Databases Processing approach:**
  This programming methodology is based on data and its movement. Program statements are defined by data rather than hard-coding a series of steps. Examples: SQL.
  
4. **Structured**:
   Programming with clean, goto-free, nested control structures. Is a kind of imperative programming where control flow is defined by nested loops, conditionals, and subroutines, rather than via gotos. Variables are generally local to blocks.
  
## [Programming language.](https://hackr.io/blog/what-is-programming-language)
A programming language is the translation from human language to machine language and is designed to carry out processes that only computers can achieve. They are used to create codes that control the behavior of the computer. These codes are expressed as algorithms as a mode of human communication. It is made up of symbols and syntactic rules that define its structure and the meaning of each expression and element. In addition there is a process which is testing, debugging, compilation and then the source code is maintained. That is called programming.
There are three types of programming language:
1. **Machine language (low level language)**:
 Collection of binary digits or bits that the computer reads and interprets (0 and 1)
2. **Assembly language (low level language)**:
  They are instructions, arithmetic operations such as ADD, SUB, DIV. Its advantages is that it has a higher encoding speed and its disadvantage is that it is not portable.
3. **High-level language**.
  Designed to make people write and understand the programs easier than the previous two. An example of them is C, Python, Java, etc.
 
## [Sequential algorithms](https://www.sciencedirect.com/topics/computer-science/sequential-algorithm)
That in which one action follows another successively. A sequence is continued from the entry and exit of the actions until the process ends.
Example:
```
#include <stdio.h>
#include <math.h>
int main (){
	float cate1, cate2, hipotenusa;
	
	printf("Ingrese los dos catetos de triangulo, por favor:\n");		scanf("%f %f",&cate1, &cate2);
	hipotenusa= sqrt(pow(cate1,2)+ pow(cate2,2));
	printf("La hipotenusa es igual a %.1f",hipotenusa);
	
	
	return 0;
}
```
## Structured programm. 
[Structured programming](https://www.geeksforgeeks.org/structured-programming-approach-with-advantages-and-disadvantages/) can be defined with a focus on where the Program is executed with a unique structure in order to be Clear, precise and to optimize time. In other words, the code works instruction after instruction. It uses only subroutines and three structures: sequence, selection (if and switch) and iteration (for and while loops). It does not support the ability to jump from one statement to another with the help of a statement like GOTO.

### Examples:
1. C
2. C ++
3. Java
4. C #  

![Ven](https://media.geeksforgeeks.org/wp-content/uploads/Programming-Approach.jpg)

## Data representations and operators.  

### Data Representation
- [**Identifier**]( http://aboutc.weebly.com/identifiers.html
): is a string of alphanumeric characters that begins with an alphabetic character or an underscore character that are used to represent various programming elements such as variables, functions, arrays, structures, unions and so on.
- [**Variables**](https://press.rebus.community/programmingfundamentals/chapter/constants-and-variables/
):  is a value that can change, depending on conditions or on information passed to the program.
- **Constants**:  is a value that cannot be altered by the program during normal execution.
- [**Reserved Words**](https://www.computerhope.com/jargon/r/reseword.htm
): are terms or phrases appropriated for special use that may not be utilized in the creation of variable names.
- [**Types of data**]( https://dl.sumdu.edu.ua/textbooks/103395/597162/index.html
): is a type together with a collection of operations to manipulate the type.
  - Primitive: are predefined types of data, which are supported by the programming language. 
    - Boolean (e.g. True or False)
    - Character (e.g. abc)
    - Date (e.g. 03/01/2017)
    - Double (e.g. 1.87651234355743E308)
    - Floating-point number (e.g. 1.23)
    - Integer (e.g. 123)
    - Long (e.g. 123456789)
    - Short (e.g. 0)
    - String (e.g. abc)
    - Void (e.g. no data)
  - **Derivied**: is one whose values are composed of component values. One example is an array.
  - **User defined**: are mathematical models of a set of data values or information that share similar behavior or qualities and that can be specified and identified independent of specific implementations. An abstract data type is defined in term of its data items or its associated operations rather than by its implementation.  
   ![data type](https://2.bp.blogspot.com/-vKeEhq3QPvA/Wvv5BGg8g1I/AAAAAAAAMSQ/-iBoXVQcI0g0tCVuMSA5IlvqqeqxQ1hjgCLcBGAs/s1600/1.jpeg)
- [**Memory space for each data type**](https://www.tutorialspoint.com/cprogramming/c_data_types.htm
):
  - Character: 1 byte
  - Unsigned character: 1 byte
  - Signed Character: 1 byte
  - Integer: 2 or 4 bytes
  - Unsigned Integer: 2 or 4 bytes
  - Short: 2 bytes
  - Unsigned Short: 2 bytes
  - Long: 8 bytes
  - Unsigned Long: 8 bytes
- [Range of values of each data type](https://xcbiology.files.wordpress.com/2015/07/table-e1438380260928.png):
  - Character: -128 to 127 or 0 to 255
  - Unsigned character: 0 to 255
  - Signed Character: -128 to 127
  - Integer: -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647
  - Unsigned Integer: 0 to 65,535 or 0 to 4,294,967,295
  - Short: -32,768 to 32,767
  - Unsigned Short: 0 to 65,535
  - Long: -9223372036854775808 to 9223372036854775807
  - Unsigned Long: 0 to 18446744073709551615
- [**Data type conversion**](https://developerinsider.co/type-casting-c-programming/
): refers to either implicitly or explicitly changing a value from one data type storage format to another, e.g. a 16-bit integer to a 32-bit integer.  
Continued there is a graphic representation about data types from [Xin's story](https://datachenblog.com/2015/07/31/cc-data-type-and-memory-management/)

![C/ c++ data types and memory](https://xcbiology.files.wordpress.com/2015/07/table-e1438380260928.png)

### Operators
- ***Conditional***: is an operator that returns one of two values depending on the result of an expression. It is represent with **“?:”**
- ***Logical***: Returns the result of a boolean operation.
  - Negation: It represents with **!**.
  - AND: It represents with **&&**.
  - Inclusive Or: It represents with **||**.
- ***Relationship***: are used to compare values of two variables.
  - Greater than >.
  - Greater than or equal to **>=**
  - Less than <
  - Less than or equal to **<=**
  - Equal to **==**
  - Not equal to **!=**
  
  Below is a descriptive image taken from the National Institute of [Open Schooling](http://oer.nios.ac.in/wiki/index.php/List_of_operators_used_in_JavaScript)
  ![List of operators in c](https://lh3.googleusercontent.com/proxy/UtM0k2eyWDmdXxG5bV7e7sxtpvYMghuY18pxA8-IzV6T3w5aJ1R0xZr5c6hD5Oo0Nw5hPYwg_v6j6D31iXG2MwQvZMPWvmrbBwCLHvAB)
  
  ## Version control.  
  
[Version control](https://www.git-tower.com/learn/git/ebook/en/command-line/basics/what-is-version-control) is a piece of software that allows a person to manage the various changes made to a file. In other words, the version control tool is used to encode versions, binary and digital files.
Version control is sometimes called revision control and is a priority component in software configuration management. 

### How Does Version Control Work?
This tool allows many developers to work together on the same protector. This happens when the project becomes more complex and there is a need to handle multiple versions.

Version control is important for all code, files, and assets that multiple team members will collaborate on. Using version control software helps you keep track of changes and keep every team member working off the latest version. 
It needs to do more than just manage and track files. It should help you develop and ship products faster. 

That’s because using the right one:  
- Improves visibility. 
- Helps teams collaborate around the world. 
- Accelerates product delivery.  

![How does it work](https://miro.medium.com/max/1248/1*l08qyjBnX7K12p4DcINn3w.png)

#### Varieties: Distributed and centralized version control.
According with Michael Ernst, [there are two types of version control](https://homes.cs.washington.edu/~mernst/advice/version-control.html), **centralized** and **distributed**. **Distributed** is  much faster to execute because it has more functions. All developers have their own copy of the repository, with all versions and all history. Of course, as they develop and make changes, their sources and versions are different from each other. However it is a little more complex and there is no main repository.  

![Distributed](https://homes.cs.washington.edu/~mernst/advice/version-control-fig3.png)  

##### Examples:
1. Git.
2. Baazaar.
3. Mercurial.
4. Darcs.  

On the other hand, in the **centralized** all the sources and their versions are stored in a single directory, which is called the source repository, of a computer (server). For this reason, developers who want to work with those fonts should ask the version control system for a local copy to work with.  

![Centralized](https://homes.cs.washington.edu/~mernst/advice/version-control-fig2.png)

##### Examples:
1. CVS.
2. Subversion.


## ***Equipo***:
1. Osiris Cámara Salinas.
2. Victor Uribe Hernandez. 
