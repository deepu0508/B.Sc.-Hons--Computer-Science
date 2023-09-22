import numpy as np

# Transpose of Matrix
def transpose(Matrix,r,c):
    NullM = []
    for i in range(r):
        n = []
        for j in range(c):
            n.insert(j,0)
        NullM.append(n)
    Transpose = np.matrix(NullM)
    
    for i in range(r):
        for j in range(c):
            Transpose[i,j] = Matrix[j,i]
    
    return Transpose

row = int(input("Enter Number of rows : "))
column = int(input("Enter Number of columns : "))
matrix = []
print("Enter values:")
for i in range(row):
    m = []
    for j in range(column):
        value = int(input(f"M{i+1}{j+1} : "))
        m.insert(j,value)
    matrix.append(m)
M = np.matrix(matrix)

print("Before Transpose Matrix \n",M)
TransM = transpose(M,row,column)
print("After Transpose of Matrix \n",TransM)
