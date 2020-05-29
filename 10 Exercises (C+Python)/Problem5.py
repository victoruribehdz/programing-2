#python code
m1=[] #Creating a list for matrix 1
m2 = [] #Creating a list for matrix 2
r = [] #Creating a list for result


#Funcion main, it is like int main(int agc, char **argv) in C programing language#
if __name__ == '__main__':
	rows = int(input('enter number of rows'));#*)#*)#,' #Asking for number of rows
	cols = int(input('enter numbers of cols')); #Asking for number of cols
	print(("Numbers of rows: %i, Number of cols: %i")%(rows, cols)) ##Print to user some info##
	for i in range(0,rows): ##This piece of code gonna add to list new  row
		m1.append([]) ##ading a new row according to respective number of rows
		m2.append([]) ##...
		r.append([])  ##The same to matrxi result
		for j in range(0,cols):
			m1[i].append(0) ##Adding a initial value to  matrix
			m2[i].append(0)
			r[i].append(0)
	print(('Matrix %ix%i\n')%(rows,cols)) ##Show some info
	print(m1)
	print(m2)
	##Getting values from keyboard##
	print("Enter values for m1: ") ##Flag
	for i in range(0,rows):
		for j in range(0,cols):
			message= "["+str(i+1)+"]"+"["+str(j+1)+"]: " ##message is a var to show the user which position is storing
			m1[i][j]=int(input(message)) ##Storing information in the respectively position
	print(m1) #Current matrix1
	print("Enter values for m2: ")
	for i in range(0,rows): ##The same that we did in the previus block but it on matrix2...
		for j in range(0,cols):
			message = "["+str(i+1)+"]"+"["+str(j+1)+"]: "
			m2[i][j]=int(input(message))
	print(m2)
	print("Result of m1 + m2: ")
	for i in range(0,rows): ##The program do some math to get the resultant matrix
		for j in range(0,cols):
			for k in range(0,cols):
				r[i][j] += m1[i][k]*m2[k][j]
	print(r) ##Print result and finish the program!
