#program that read a file with numbers and create files with the fizzbuzz test
fb = open('fizzbuzz.txt', 'w')    #open files
f = open('fizz.txt', 'w')
b = open('buzz.txt', 'w')
nfb = open('nofizzbuzz.txt', 'w')
with open ('numbers.txt', 'r') as file: #read the content of the file
  print("Reading numbers\n")
  for num in file:  #for the content of the file check the conditions
    num = int(num)  #convert string to an integer
    if ((num % 5 == 0) and (num % 3 == 0)):  #if the number could be divide by 5 and 3 exactly write in fizzbuzz document
        fb.write(str(num)+"\n") #convert the number to string and write in the file
    elif(num % 3 == 0):       #if the number could be divide by 3 exactly write in fizz document
        f.write(str(num)+"\n")  #convert the number to string and write in the file
    elif(num % 5 == 0): #if the number could be divide by 5 exactly write in buzz document
        b.write(str(num)+"\n")  #convert the number to string and write in the file
    else:   #if the number could not be divide by 5 or 3 exactly write in nofizzbuzz document
        nfb.write(str(num)+"\n")    #convert the number to string and write in the file
print("Numbers written succesfully")
fb.close()    #close documents
f.close()
b.close()
nfb.close()