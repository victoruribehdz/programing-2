'''
1. Calculate the Euler constant e using the series:
https://wikimedia.org/api/rest_v1/media/math/render/svg/698f402ad56c5162a9280b6aaa8eb79acbc49550
'''
number = int(input("number: ")) #Type a number
sum = 0 #Declare variables
x = 1
factorial = 1
for i in range(1, number+2): #This process is going to be make only between 1 and the number typed plus two
    sum = sum + (1/factorial)
    factorial *= i
print(round(sum, 2))    #Print all the proceeses