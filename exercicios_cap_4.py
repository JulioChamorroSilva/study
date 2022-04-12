import scipy.linalg as sl
from scipy import *
from matplotlib.pyplot import *
from numpy import *
print("\nExercício 1:\n")
# Construct this matrix in Python using the function array .

M1=array([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]])
print(M1)          
# Construct the same matrix using the function arange followed by a suitable reshape
M2=arange(1,13)
M2=M2.reshape(4,3)
print(M2)

#What is the result of the expression M[2,:] ? What is the result of the similar expression M[2:]?
print(M1[2,:]) #retorna somente a linha 2
print(M1[2:]) #retorna todos os valores após a linha 2
print("\nExercício 2:\n")
#Given a vector x, construct in Python the following matrix:

x=array([0.0,0.5,1.,1.5,2.,2.5])
y=array([-2.,0.5,-2.,1.,-0.5,1.])
V=column_stack([x**5,x**4,x**3,x**2,x**1,x**0]) #aqui se cria uma Vandermonde matrix
a=np.linalg.solve(V, y)
def p(k):
    return sum([a[5-i]*k**i for i in range(6)])
z = np.linspace(0, 2.5, 6)
vecV=np.vectorize(p)
plot(z,vecV(z),'b', label='Exercício 2') 
plot(x,y,'r*')

print("\nExercício 3:\n")
# Repeat Ex. 2 by using these commands.
x2=array([0.0,0.5,1.,1.5,2.,2.5])
y2=array([-2.,0.5,-2.,1.,-0.5,1.])
V2 = np.vander(x2, N = 6) #aqui se cria uma Vandermonde matrix
a2=np.linalg.solve(V2, y2)
def p2(k):
    return polyval(a2,k) 
z2 = np.linspace(0, 2.5, 200)
vecV2=np.vectorize(p2)
plot(z2,vecV2(z2),'g', label='Exercício 3')

print("\nExercício 4:\n")
#Let u be a one dimensional array. Construct another array ξ with values ξi = (u1 + ui+1+ ui+2)/3. 
u=array(arange(10))
def epsi(j):
    return (u[j]+u[j+1]+u[j+2])/3


print("\nExercício 5:\n")
#Construct from the matrix V given in Ex. 2 a matrix A by deleting V's first column
A=V[:,1:]
#Form the matrix B = (AT A)-1 AT.
B=(np.linalg.inv(A.T@A))@A.T
#Compute c = B y with y from Ex. 2.
c=dot(B,y)
#Use c and polyval to plot the polynomial defined by c. Plot in the same picture again the points (xi, yi)
def p3(k):
    return polyval(c,k)
z3 = np.linspace(0, 2.5, 200)
vecV3=np.vectorize(p3)
plot(z3,vecV3(z3),'r', label='Exercício 5')

print("\nExercício 6:\n")
#Ex. 5 describes the least square method. Repeat that exercise but use SciPy's scipy.linalg.lstsq method instead.
m, con, *temp = np.linalg.lstsq(V,x,rcond=None)[0]
plot(x,y*m+con,'c', label='Exercício 6')



