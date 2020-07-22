#FizzBuzz
#FizzBuzz vectorized
import numpy as np 
from datetime import datetime

start_time = datetime.now() #start counting the time

fb = np.arange(start = 9, stop = 151)     #define an array from 9 to 151
print(fb[((fb % 5 == 0) & (fb % 3 == 0))])  #Print the fizzbuzz numbers that met the condition.
print(f"\n The total of fizzbuzz numbers is: {np.sum((fb % 5 == 0) & (fb % 3 == 0))}")
#Count the number of fizzbuzz numbers and print the counter

end_time = datetime.now()   #end counting the time
print("\n Duration: {}".format(end_time - start_time))  #substract the start time to the finish time and print the duration
#The duration average was 0:00:00.000573

#FizzBuzz using for loop
"""
counter = 0
for fb in range (9, 151):
    if((fb % 5 == 0) & (fb % 3 == 0)):
        print(f"{fb}\n")
        counter =+ 1
print(f"The total of fizzbuzz numbers is: {counter}")
"""
# The duration average was 0:00:00.003715

#In conclusion with vectorization was faster than with the normla loops