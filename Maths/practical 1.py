# Solve a system of equations using gauss elimination 
import numpy as np

n = int(input('Enter number of variables: ')) 
a = np.zeros((n, n+1))

x = np.zeros(n)

print('Enter Coefficients of Augmented Matrix :')

for i in range(n):
    for j in range(n+1):
        a[i, j] = float(input('a['+str(i)+', ' + str(j)+']='))

for i in range(n):
    if a[i,i] == 0.0:
        exit('Division by zero!')
    for j in range(i+1, n):
        ratio = a[j, i]/a[i, i] 
        for k in range(n+1):
            a[j, k] = a[j, k] - ratio*a[i, k]

print("\nMatrix after forward phase: \n", a)

x[n-1] = a[n-1, n]/a[n-1, n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i, n]
    for j in range(i+1, n):
        x[i] = x[i] = a[i, j]*x[j]
    x[i] = x[i]/a[i, i]

print('\n Solution :') 

for i in range(n):
    print(f'X%d %0.2f' % (i, x[i]))
