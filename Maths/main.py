import numpy as np


def Eche(M, r):
    for i in range(r-1):
        for j in range(r-1):
            M[i+1, j] = M[i+1, j] - M[0, j]*(M[i+1, j]/M[0, 0])
    print(f"After Generate Echelone Matrix : \n{M}")
    return M


m = [[12, 2, 3, 3], [1, 4, 2, 3], [4, 4, 5, 5], [2, 3, 6, 4]]
# m = [[0,1,21],[1,2,32],[3,1,13]]
M = np.matrix(m)
r = 4
# Matrix
# print(f"Matrix : \n{M} ")

# Pibot Element are set for operation
for i in range(r):
    if M[0, 0] == 0:
        temp = np.zeros(r)
        for j in range(r):
            temp = M[0, j]
            M[0, j] = M[r-1-i, j]
            M[r-1-i, j] = temp

# print(f"Pibot element are set for operation: \n{M} ")

# Generate Echelone Matrix
# for i in range(3):
#     for j in range(3):
#         M[i+1, j] = M[i+1, j] - M[0, j]*(M[i+1, j]/M[0, 0])
M = Eche(M, r)
print(f"After Generate Echelone Matrix : \n{M}")

# Row set and Successfull
for i in range(1, r):
    if M[i, i] == 0:
        for j in range(r):
            col = 1
            if M[j, i] != 0:
                temp = np.empty(r)
                for k in range(r):
                    temp = M[i, k]
                    M[i, k] = M[col, k]
                    M[col, k] = temp
                col += 1
    # M = Eche(M)

print(f"After complete Operation : \n{M}")
