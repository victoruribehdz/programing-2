def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): ## ":" Missing
#def print_first_word(words)
    """Prints the first word after popping it off."""
    #word = words.poop(0)
    word = words.pop(0) # it is .pop
    print (word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    #word = words.pop(-1
    word = words.pop(-1) ## ")" Missing
    print (word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print ("Let's practice everything.")
print ('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print ("--------------")
print (poem)
print ("--------------")

#five = 10 - 2 + 3 - 5
five = 10 - 2 + 3 - 6 ## I changed the 5 and I put 6 to give the result.
print ("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    #jars = jelly_beans \ 1000
    jars = jelly_beans / 1000 #The slash was wrong
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#beans, jars, crates == secret_formula(start-point)
beans, jars, crates = secret_formula(start_point) #The line would be down.

print ("With a starting point of: %d" % start_point)
#print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)
print ("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)) #It is not jeans, is beans.

start_point = start_point / 10

print ("We can also do that this way:")
#print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_pont
print ("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)) #")" Missing

#sentence = "All god\tthings come to those who weight."
sentence = "All good things come to those who wait." #This slash should not be in the sentence.

#Print the first and last word of the sentence

#words = ex25.break_words(sentence)
words = break_words(sentence) ##We don't need to import from exercise 25, we already have it in the functions. Break_words function.
#sorted_words = ex25.sort_words(words)
sorted_words = sort_words(words) ##We don't need to import from exercise 25, we already have it. Sort_words function

print_first_word(words)
print_last_word(words)
#.print_first_word(sorted_words)
print_first_word(sorted_words) ##This point should not be there
print_last_word(sorted_words)
#sorted_words = ex25.sort_sentence(sentence)
sorted_words = sort_sentence(sentence) #We don't need to import from exercise 25, we already have it. Sorted_words function.
#prin sorted_words
print (sorted_words) #the word is 'print' and "()" Missing

print_first_and_last(sentence)
#   print_first_a_last_sorted(senence)
print_first_and_last_sorted(sentence) #the space is wrong, is 'and' no 'a', identification
