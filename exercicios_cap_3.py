from scipy import *
from matplotlib.pyplot import *
from numpy import *
#Exercícios do livro Scientific computing with python 3, capítulo 3
# Execute the following statements:
print("Exercício 1:\n")    
L = [1, 2]
L3 = 3*L
print(L3)
# Try to predict the outcome of the following commands:
L3[0] # Retorna 1
L3[-1] #Retorna 2
# L3[10] retorna um erro de index
# What does the following command do?
L4 = [k**2 for k in L3] #Eleva todos os itens da lista L3 ao quadrado para a lista L4
print(L4) 
# Concatenate L3 and L4 to a new list L5.
L5 = L3 + L4
print(L5)
print("\nExercício 2:\n")
#Use the range command and a list comprehension to generate a list with 100
# equidistantly spaced values between 0 and 1.
Var1 = list(range(0,101,1))
Var2 = [k/100 for k in Var1]
print(Var2)
print("\nExercício 3:\n")
# Assume that the following signal is stored in a list:
L = [0,1,2,1,0,-1,-2,-1,0]
# What is the outcome of:
L[0] #Será 0
L[-1] #Será 0
L[:-1] #Será todos os números exceto o último
L + L[1:-1] + L #Será uma lista composta pela lista L seguida pelos números entre o termo 1 até o penúltimo seguida pela lista L novamente
L[2:2] = [-3] #O termo 2 será substituido por -3
L[3:4] = [] #O termo 3 será apagado
L[2:5] = [-5] #Os termos 2, 3 e 4 serão substituídos por -5
# Do this exercise by inspection only, that is, without using your Python Shell
print("\nExercício 4:\n")
# Consider the Python statements:
m=1
L = [n-m/2 for n in range(m)]
ans = 1 + L[0] + L[-1] #Independente do valor de m o resultado sempre será 1
#and assume that the variable m has been previously assigned an integer value. What is the
#value of ans? Answer this question without executing the statements in Python.
print("\nExercício 5:\n")


# Consider the recursion formula:
#Create a list u. Store in its first three elements e0, eha, and e2ha. These represent the starting values u0, u1, and u2 in the given formula. Build up the complete list from the recursion formula.
#Construct a second list, td, in which you store the values nh, with n = 0, …, 1000. Plot td versus u (refer section Basic plotting in Chapter 6, Plotting, for more information). Make a second plot in which you plot the difference, that is, |eatn– u n|, where tn represents the values inside the vector td . Set axis labels and a title
h=1./1000.
a=-0.5
u=[exp(0),exp(h*a),exp(2*h*a)]
td=[0, 1*h, 2*h]
for n in range(1000):
    ulistadd = u[n+2]+h*a*((23/12)*u[n+2]-(4/3)*u[n+1]+(5/12)*u[n])
    u.append(ulistadd)
    td.append((n+3)*h)
plot(td, u)
# > Esse trecho eu não entendi o que quis dizer por plottar a diferença > plot the difference, that is, |eatn–u n|
print("\nExercício 6:\n")

# Let A and B be sets. The set (A \ B) ∪ (B \ A) is called the symmetric difference of the two sets. Write a function that performs this operation. Compare your results to the result of the command:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = A.difference(B)
D = B.difference(A)
F = C.union(D)
print(F)
print(A.symmetric_difference(B))
print("\nExercício 7:\n")

#Study other operations on sets. You find a complete list of those by using the command completion feature of IPython. In particular, study the update and intersection_update methods. What is the difference between intersection and intersection_update?
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

result = A.intersection_update(B)

print('result =', result)
print('A =', A)
print('B =', B)
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

result = A.intersection(B)

print('result =', result)
print('A =', A)
print('B =', B)
#Intersection retorna a interceção enquanto intersection_update atualiza o primeiro set