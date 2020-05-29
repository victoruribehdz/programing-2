'''
DESCRIPTION:
Check the validity of a password (input from users)
Validation: 
• At least 1 letter between [a-z] and 1 letter between [A-Z]. 
• At least 1 number between [0-9]. 
• At least 1 at least one punctuation sign. 
• Minimum length 6 characters
'''

import re ##I import regulated expressions, that is, they can be evaluated in a module

punctuation_sign= ['$', '#', '@', '?', '¿', '!', '¡', '&', '%'] #I establish what the punctuation marks I want
password= input("Input your password, please: ") #Input
validity= True ##I want this boolean to verify my password requirements 
tamaño= len(password) ##Get the size of my password


while validity: ##While this gives false the password is not correct and breaks occur, that is, the program ends
    if (tamaño<6 or tamaño>16): ##I want the password size to be minimum 6 and maximum 16
        print('Password to have at least 6 letters and a maximun of 16')
        break
    if not (i.isupper() for i in password): ## function any returns T if any element of an iterable is T. If not, any returns F.
        print('Password needs at least one uppercase letter')  ## I use .upper to check each letter of the password for uppers
        break ##If this happens then 
    if not (i.islower() for i in password): ##I use .slower to check each iteration in the for if there are lowercase
        print('Password needs at least one lowercase letter')  ##I print if this condition is not found (IF NOT)
        break #Close the program
    if not re.search("[0-9]",password): #With re, check if the pattern matches the pattern. So we see the search
        print('Password needs at least a number between 1-9') 
        break
    if not any (i in punctuation_sign for i in password): #If after loop for, a punctuation mark is not found in the password
        print('Password needs at least one symbol') #Print
        break #close program
    else: # I do not enter these if it is because everything is fine, then go to the else and the password is valid
      print(f"Your password is valid: {password}") #print
      break #Close the program