# Add, Substraction, Multiplication abd division of randoom vectors.
import numpy as np 

def vector_op(x, y):
  sub = x - y
  add = x + y
  div = x / y
  mult = x * y
  print(add)
  print(sub)
  print(mult)
  print(div)

np.random.seed(10)
a = np.random.randint(10, size=5)
b = np.random.randint(10, size=5)
print(a)
print(b)

print(vector_op(a, b))