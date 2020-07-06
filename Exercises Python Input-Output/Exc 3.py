#program that create a file, write text and append more text
with open ('Lasagna.txt', 'w') as file:     #create the file
  text = str(input('Type content for the file: '))  #the user type content for the file in the console
  file.write(str(text)+"\n")    #write the content in the file
file.close()    #close the file
with open ('Lasagna.txt', 'a') as file:     #open the file again
  text2 = str(input('Type more content for the file: '))    #the user type more content for the file in the console
  file.write(str(text2))    #write the new content in the file
file.close()    #close the file