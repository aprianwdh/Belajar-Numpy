import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
print(a)
a = np.array([1,0.2,0.3,5.5])
print(a)

# vector dengan range
# (start,stop,step)
b = np.arange(2,10,2)
print(b)

# array linspace
c = np.linspace(1,10,4)
print(c)

# membuat matriks
d = np.array([(1,2,3,4),
              (2,3,4,5),
              (9,12,39,21)])

print(d)

# membuat matriks dengan nilai 0
e = np.zeros((4,4))
print(e)

# membuat matriks dengan nilai 1
f = np.ones((4,4))
print(f)

# membuat matriks indetity
g = np.identity(4)
print(g)
