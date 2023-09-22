import numpy as np
# -------------->>>>>>>>>>> ALERT : This program is successfully work only this Matrix

m = [[0, 2, 3, 3], [1, 4, 2, 3], [4, 4, 5, 5], [0, 3, 6, 4]]
M = np.matrix(m)
r = 4
# Matrix
print(f"Matrix : \n{M} ")

# Pibot Element are set for operation
for i in range(4):
    if M[0, 0] == 0:
        temp = np.zeros(4)
        for j in range(4):
            temp = M[0, j]
            M[0, j] = M[3-i, j]
            M[3-i, j] = temp        
print(f"Pibot element are set for operation: \n{M} ")

# Generate Echelone Matrix
for i in range(3):
    for j in range(3):
        M[i+1, j] = M[i+1, j] - M[0, j]*(M[i+1, j]/M[0, 0])
print(f"After Generate Echelone Matrix : \n{M}")


# Row set and Successfull
for i in range(1, 4):
    for j in range(4):
        col = 1
        if M[j, i] != 0:
            temp = np.empty(4)
            for k in range(4):
                temp = M[i, k]
                M[i, k] = M[col, k]
                M[col, k] = temp
            col += 1
    # M = Eche(M)
print(f"After complete Operation : \n{M}")
