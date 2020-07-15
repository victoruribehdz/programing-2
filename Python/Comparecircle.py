import math
def circle_area(r):
  area= (r**2)*math.pi
  print(area)


a = int(input("Type the fist radio: "))
b = int(input("Type the second radio: "))

print(circle_area(a))
print(circle_area(b))

if a > b:
  print("The first circle is greater than the second")
else:
  print("The second circle is greather than the first")
