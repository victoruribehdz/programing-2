#Given a list of strings delete all special chars in each one (non-alphanumeric chars).
ini_string = "Ay%mi/madre$el?comandante#CR7*" #Type the string
print ("initial string : ", ini_string) #Print the initial string
getVals = list([val for val in ini_string if val.isalnum()]) #Delete all the special characters
result = "".join(getVals) 
print ("final string", result) #Print the string without the special characters.