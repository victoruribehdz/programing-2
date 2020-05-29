'''
Count the Word Frequency in a Text (Unique String). Don’t forget to: normalize to
lower case and delete special chars.
Expected Output: Frequency of pizza is 4
'''
def freq(str):  #Define a function
    str_list = str.split() 
    unique_words = set(str_list) 
    for words in unique_words : #For words that are found in the list print the frequency of the words
        print('Frequency of ', words , 'is :', str_list.count(words)) 
if __name__ == "__main__": 
    str ='pizza salad burguer pizza pizza burguer pizza salad' #Here type the words
    freq(str) 