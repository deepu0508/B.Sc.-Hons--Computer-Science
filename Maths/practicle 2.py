import numpy as np
# Generate Inverse

# Inverse of Matrix
m = [[2, 4, 5], [5, 6, 2], [7, 2, 4]]
M = np.matrix(m)

# Determinent
detM = 0
for i in range(3):
    temp = M
    temp = np.delete(temp,0,0)
    temp = np.delete(temp,i,1)
    v = temp[0,0]*temp[1,1] - temp[0,1]*temp[1,0]
    if (i+1)%2 == 0:
        detM += (-1)*M[0,i]*v
    else:
        detM += M[0, i]*v

# print(detM)
cofactor = np.eye(3)

for i in range(1,4):
    for j in range(1,4):
        temp = M
        temp = np.delete(temp,i-1,0)
        temp = np.delete(temp,j-1,1)
        cofactor[i-1, j-1] = np.linalg.det(temp)*((-1)**((i)+(j)))
print(np.linalg.inv(M))

invM = (1/detM)*cofactor
print(invM)
