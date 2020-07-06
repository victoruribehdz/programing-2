#program that read a file with numbers and create files with odd and even.
even = open('even.txt', 'w')    #open files
odd = open('odd.txt', 'w')
with open ('numbers.txt', 'r') as file: #read the content of the file
  print("Reading numbers\n")
  for num in file:  #for the content of the file check the conditions
    num = int(num)  #convert string to an integer
    if (num % 2 == 0):  #if the number could be divide by 2 exactly write in even document
      even.write(str(num)+"\n") #convert the number to string and write in the file
    else:       #if the number could not be divide by 2 exactly write in odd document
      odd.write(str(num)+"\n")  #convert the number to string and write in the file
print("Numbers written succesfully")
even.close()    #close documents
odd.close()