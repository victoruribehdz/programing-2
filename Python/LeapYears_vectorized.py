#Leap years
#Leap years vectorized
import numpy as np 
from datetime import datetime

start_time = datetime.now() #start counting the time

year = np.arange(start = 1900, stop = 2151)     #define an array from 1900 to 2151
print(year[((year % 400 == 0) | (year % 4 == 0) & (year % 100 != 0))])  #Print the years that met the condition.
print(f"\n The total leap years is: {np.sum((year % 400 == 0) | (year % 4 == 0) & (year % 100 != 0))}")
#Count the number of years and print the counter

end_time = datetime.now()   #end counting the time
print("\n Duration: {}".format(end_time - start_time))  #substract the start time to the finish time and print the duration
#The duration average was 0:00:00.000693

#Leap years using for loop
"""
counter = 0
for year in range (1900, 2151):
    if((year % 400 == 0) | (year % 4 == 0) & (year % 100 != 0)):
        print(f"{year}\n")
        counter =+ 1
print(f"The total of leap year is: {counter}")
"""
# The duration average was 0:00:00.002378

#In conclusion with vectorization was faster than with the normla loops