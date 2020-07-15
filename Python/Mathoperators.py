def math_operators(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div= x / y
    print (add)
    print (sub)
    print (mul)
    print (div)


a = int(input("Type the fist number: "))
b = int(input("Type the second number: "))
c = int(input("Type the third number: "))
d = int(input("Type the fourth number: "))

print (math_operators(a, b))
print (math_operators(c, d))
print (math_operators(a, c))
print (math_operators(b, d))
print (math_operators(a, d))
print (math_operators(b, c))
